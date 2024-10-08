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
import os

os.environ["OTEL_SDK_DISABLED"] = "true"

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

@app.post("/process-code")
async def process_code_endpoint(code_input: CodeInput):
    analysis_result = await analyze_code(code_input)
    refactoring_result = await refactoring_code(code_input, analysis_result)
    test_result = await perform_test(code_input, analysis_result, refactoring_result)
    scan_result = await perform_scan_vulnerability(code_input)

    return {
        "analysis_result": analysis_result,
        "refactoring_result": refactoring_result,
        "test_result": test_result,
        "scan_result": scan_result
    }


def process_code_string(code: str) -> Dict[str, Any]:
    analysis_result = analyze_code(code)
    refactoring_result = refactoring_code(code, analysis_result)
    test_result = perform_test(code, analysis_result, refactoring_result)
    scan_result = perform_scan_vulnerability(code)

    return {
        "analysis_result": analysis_result,
        "refactoring_result": refactoring_result,
        "test_result": test_result,
        "scan_result": scan_result
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

async def process_zip_file(zip_contents: bytes, task_id: str):
    # Create a ZipFile object from the in-memory file
    with zipfile.ZipFile(io.BytesIO(zip_contents)) as zip_ref:
        # Initialize an empty string to store all code
        all_code = ""

        # Iterate through all files in the zip
        for file_name in zip_ref.namelist():
            # Skip directories
            if file_name.endswith('/'):
                continue

            # Read the content of each file
            with zip_ref.open(file_name) as file:
                try:
                    # Try to decode the file content as UTF-8
                    code_content = file.read().decode('utf-8')
                    # Append the code content to all_code with a separator
                    all_code += f"\n\n# File: {file_name}\n\n{code_content}"
                except UnicodeDecodeError:
                    # If decoding fails, it's likely a binary file, so we skip it
                    continue

    # Process all the code as a single string
    result = process_code_string(all_code)
    print(f"##########Analysis Result##########\n{result['analysis_result']}\n\n\n\n"
          f"##########Refactoring Result##########\n{result['refactoring_result']}\n\n\n\n"
          f"##########Test Result##########\n{result['test_result']}\n\n\n\n"
          f"##########Scan Result##########\n{result['scan_result']}")

    task_results[task_id] = {"status": "completed", "result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    result = process_code_string("""
""")
    print(f"##########Analysis Result##########\n{result['analysis_result']}\n\n\n\n"
          f"##########Refactoring Result##########\n{result['refactoring_result']}\n\n\n\n"
          f"##########Test Result##########\n{result['test_result']}\n\n\n\n"
          f"##########Scan Result##########\n{result['scan_result']}")
