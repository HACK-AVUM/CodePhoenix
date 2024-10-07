from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from system_agent_analysis.src.crews.quality_control_crew import analyze_code
from system_agent_refactoring.src.crews.refactor_crew import refactoring_code
from system_agent_test.app.services.test_service import perform_test
from system_agent_scanning_vuln.app.services.scanning_vulnerability_service import perform_scan_vulnerability
import os

os.environ["OTEL_SDK_DISABLED"] = "true"

app = FastAPI()

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

if __name__ == "__main__":
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    print(process_code_string("print('Hello, World!')"))
