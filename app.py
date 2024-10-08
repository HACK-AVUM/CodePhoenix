import os

os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["TOGETHERAI_API_KEY"] = "c47b3fa9622715d6695302a193d0488be41d61660b82ca6502eb45c61efce2c9"

os.environ["LLM"] = "together_ai/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"


import subprocess
from time import sleep
from fastapi import FastAPI, UploadFile, BackgroundTasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import zipfile
import io
from fastapi import UploadFile
import uuid
from system_agent_analysis.src.crews.quality_control_crew import analyze_code
from system_agent_refactoring.src.crews.refactor_crew import refactoring_code
from system_agent_test.app.services.test_service import perform_test
from system_agent_scanning_vuln.app.services.scanning_vulnerability_service import perform_scan_vulnerability
import requests
from datetime import datetime, timezone



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class CodeInput(BaseModel):
    code: str

class RefactorInput(BaseModel):
    code: str
    analysis_result: str

class TestInput(BaseModel):
    old_code: str
    old_code_analysis_result: str
    new_code_to_test: str


@app.post("/analyze")
async def analyze_code_endpoint(code_input: CodeInput):
    return analyze_code(code_input.code)

@app.post("/refactor")
async def refactor_code_endpoint(refactor_input: RefactorInput):
    return refactoring_code(refactor_input.code, refactor_input.analysis_result)


@app.post("/test")
async def test_code_endpoint(test_input: TestInput):
    return perform_test(test_input.old_code, test_input.old_code_analysis_result, test_input.new_code_to_test)

@app.post("/scan-vulnerabilities")
async def scan_vulnerabilities_endpoint(code_input: CodeInput):
    return perform_scan_vulnerability(code_input.code)


# @app.post("/generate-documentation", response_model=ServiceResponse)
# async def generate_documentation(code_input: CodeInput):
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f"{DOC_SERVICE_URL}/generate_documentation", json={"codeSnippet": code_input.code})
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Documentation generation service error")
#     return ServiceResponse(status="success", result=response.json())


def process_code_string(code: str) -> Dict[str, Any]:
    analysis_result = analyze_code(code)
    scan_result = perform_scan_vulnerability(code)
    refactoring_result = refactoring_code(code, analysis_result)
    test_result = perform_test(code, analysis_result, refactoring_result)



    return {
        "analysis_result": analysis_result,
        "scan_result": scan_result,
        "refactoring_result": refactoring_result,
        "test_result": test_result,
    }


task_results = {}

class TaskStatus(BaseModel):
    status: str
    result: dict = None

@app.post("/process-zip")
async def process_zip_endpoint(zip_file: UploadFile, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    task_results[task_id] = {"status": "processing"}

    # Read the uploaded file into memory
    zip_contents = await zip_file.read()

    background_tasks.add_task(process_zip_file, zip_contents, task_id)

    return {"task_id": task_id}

@app.get("/task/{task_id}", response_model=TaskStatus)
async def get_task_status(task_id: str):
    if task_id not in task_results:
        return {"status": "not_found"}
    return task_results[task_id]


def process_zip_file(zip_contents: bytes, task_id: str):
    # Create a local directory to extract the zip contents
    code_dir = "./code"
    os.makedirs(code_dir, exist_ok=True)

    try:
        # Create a ZipFile object from the in-memory file and extract its contents
        with zipfile.ZipFile(io.BytesIO(zip_contents)) as zip_ref:
            zip_ref.extractall(code_dir)

        # Run SonarQube scan
        sonar_scanner_cmd = [
            "sonar-scanner",
            f"-Dsonar.projectKey=prova",
            f"-Dsonar.sources={code_dir}",
            "-Dsonar.host.url=http://sonarqube:9000",
            "-Dsonar.token=sqp_638686bd282aa7716f2ae228a3a014f0e62e3ef1"
        ]

        try:
            process = subprocess.run(
                sonar_scanner_cmd,
                capture_output=True,
                text=True,
                check=True
            )
            scan_result = process.stdout
        except subprocess.CalledProcessError as e:
            scan_result = f"Error SonarQube scan: {e.stderr}"
        except Exception as e:
            scan_result = f"Error running SonarQube scan: {str(e)}"

        sleep(2)

        # Process the code as before
        all_code = ""
        for root, _, files in os.walk(code_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        code_content = file.read()
                        all_code += f"\n\n# File: {os.path.relpath(file_path, code_dir)}\n\n{code_content}"
                except UnicodeDecodeError:
                    continue

        # Fetch SonarQube results if scan was successful
        if "Error" not in scan_result:
            sonarqube_api_url = f"http://sonarqube:9000/api/issues/search?componentKeys=prova"

            print(sonarqube_api_url)

            try:
                headers = {
                    "Authorization": "Bearer sqp_638686bd282aa7716f2ae228a3a014f0e62e3ef1"
                }
                response = requests.get(sonarqube_api_url, headers=headers)
                if response.status_code == 200:
                    sonarqube_results = response.json()
                    all_code += f"\n\n# SonarQube Analysis Results\n\n{sonarqube_results}"
                else:
                    print(f"Failed to fetch SonarQube results: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error fetching SonarQube results: {str(e)}")




        result = {}

        difficulty_rating = analyze_code(all_code, number_response=True)


        result["LLM used"] = "Llama 3.1 7B Instruct"

        try:
            difficulty = int(difficulty_rating)
            if difficulty > 7:
                print(f"Code difficulty: {difficulty}")
                os.environ["LLM"] = "together_ai/meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
                result["LLM used"] = "Llama 3.1 70B Instruct"
        except ValueError:
            print("Invalid difficulty rating")


        result.update(process_code_string(all_code))

        to_repeat = perform_test(all_code, result["analysis_result"], result["refactoring_result"], binary_response=True)
        if to_repeat == "1":
            print("Repeating the task")
            result.update(process_code_string(all_code))


        print(f"##########Analysis Result##########\n{result['analysis_result']}\n\n\n\n"
              f"##########Refactoring Result##########\n{result['refactoring_result']}\n\n\n\n"
              f"##########Test Result##########\n{result['test_result']}\n\n\n\n"
              f"##########Scan Result##########\n{result['scan_result']}")

        task_results[task_id] = {"status": "completed", "result": result}

    finally:
        # Clean up: delete the local directory after analysis
        import shutil
        shutil.rmtree(code_dir, ignore_errors=True)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=60000)
    result = process_code_string("""
""")
    print(f"##########Analysis Result##########\n{result['analysis_result']}\n\n\n\n"
          f"##########Refactoring Result##########\n{result['refactoring_result']}\n\n\n\n"
          f"##########Test Result##########\n{result['test_result']}\n\n\n\n"
          f"##########Scan Result##########\n{result['scan_result']}")
