from textwrap import dedent

from fastapi import FastAPI
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
    result = process_code_string("""
           IDENTIFICATION DIVISION.
       PROGRAM-ID. INVENTORY-MANAGEMENT.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT PRODUCT-FILE ASSIGN TO "PRODUCTS.DAT"
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  PRODUCT-FILE.
       01  PRODUCT-RECORD.
           05  PRODUCT-ID       PIC 9(5).
           05  PRODUCT-NAME     PIC X(30).
           05  PRODUCT-QUANTITY PIC 9(5).
           05  PRODUCT-PRICE    PIC 9(5)V99.

       WORKING-STORAGE SECTION.
       77  WS-OPTION           PIC 9.
       77  WS-PRODUCT-ID       PIC 9(5).
       77  WS-PRODUCT-NAME     PIC X(30).
       77  WS-PRODUCT-QUANTITY PIC 9(5).
       77  WS-PRODUCT-PRICE    PIC 9(5)V99.
       77  WS-EOF              PIC X VALUE 'N'.

       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM INIT-PARA.
           PERFORM UNTIL WS-OPTION = 4
               DISPLAY "MENU OPTIONS"
               DISPLAY "1. ADD PRODUCT"
               DISPLAY "2. UPDATE PRODUCT"
               DISPLAY "3. VIEW ALL PRODUCTS"
               DISPLAY "4. EXIT"
               ACCEPT WS-OPTION
               EVALUATE WS-OPTION
                   WHEN 1
                       PERFORM ADD-PRODUCT-PARA
                   WHEN 2
                       PERFORM UPDATE-PRODUCT-PARA
                   WHEN 3
                       PERFORM VIEW-PRODUCTS-PARA
                   WHEN 4
                       DISPLAY "EXITING PROGRAM."
                   WHEN OTHER
                       DISPLAY "INVALID OPTION. TRY AGAIN."
               END-EVALUATE
           END-PERFORM.
           STOP RUN.

       INIT-PARA.
           OPEN I-O PRODUCT-FILE
           IF STATUS-CODE NOT = 0
               DISPLAY "ERROR OPENING FILE."
               STOP RUN
           END-IF.

       ADD-PRODUCT-PARA.
           DISPLAY "ENTER PRODUCT ID: " 
           ACCEPT WS-PRODUCT-ID
           DISPLAY "ENTER PRODUCT NAME: " 
           ACCEPT WS-PRODUCT-NAME
           DISPLAY "ENTER PRODUCT QUANTITY: " 
           ACCEPT WS-PRODUCT-QUANTITY
           DISPLAY "ENTER PRODUCT PRICE: " 
           ACCEPT WS-PRODUCT-PRICE

           MOVE WS-PRODUCT-ID TO PRODUCT-ID
           MOVE WS-PRODUCT-NAME TO PRODUCT-NAME
           MOVE WS-PRODUCT-QUANTITY TO PRODUCT-QUANTITY
           MOVE WS-PRODUCT-PRICE TO PRODUCT-PRICE

           WRITE PRODUCT-RECORD
               DISPLAY "PRODUCT ADDED."

       UPDATE-PRODUCT-PARA.
           DISPLAY "ENTER PRODUCT ID TO UPDATE: "
           ACCEPT WS-PRODUCT-ID
           PERFORM FIND-PRODUCT

           IF WS-EOF = 'Y'
               DISPLAY "PRODUCT NOT FOUND."
           ELSE
               DISPLAY "ENTER NEW PRODUCT NAME: "
               ACCEPT WS-PRODUCT-NAME
               DISPLAY "ENTER NEW PRODUCT QUANTITY: "
               ACCEPT WS-PRODUCT-QUANTITY
               DISPLAY "ENTER NEW PRODUCT PRICE: "
               ACCEPT WS-PRODUCT-PRICE

               MOVE WS-PRODUCT-ID TO PRODUCT-ID
               MOVE WS-PRODUCT-NAME TO PRODUCT-NAME
               MOVE WS-PRODUCT-QUANTITY TO PRODUCT-QUANTITY
               MOVE WS-PRODUCT-PRICE TO PRODUCT-PRICE

               REWRITE PRODUCT-RECORD
                   DISPLAY "PRODUCT UPDATED."
           END-IF.

       VIEW-PRODUCTS-PARA.
           DISPLAY "PRODUCT LIST:"
           PERFORM UNTIL WS-EOF = 'Y'
               READ PRODUCT-FILE INTO PRODUCT-RECORD
                   AT END
                       MOVE 'Y' TO WS-EOF
                   NOT AT END
                       DISPLAY "ID: " PRODUCT-ID " NAME: " PRODUCT-NAME
                           " QUANTITY: " PRODUCT-QUANTITY
                           " PRICE: " PRODUCT-PRICE
               END-READ
           END-PERFORM.

       FIND-PRODUCT.
           MOVE 'N' TO WS-EOF
           REWRITE PRODUCT-RECORD
           PERFORM UNTIL WS-EOF = 'Y'
               READ PRODUCT-FILE INTO PRODUCT-RECORD
                   AT END
                       MOVE 'Y' TO WS-EOF
                   NOT AT END
                       IF WS-PRODUCT-ID = PRODUCT-ID
                           EXIT PERFORM
                       END-IF
               END-READ
           END-PERFORM.
""")
    print(f"##########Analysis Result##########\n{result['analysis_result']}\n\n\n\n"
          f"##########Refactoring Result##########\n{result['refactoring_result']}\n\n\n\n"
          f"##########Test Result##########\n{result['test_result']}\n\n\n\n"
          f"##########Scan Result##########\n{result['scan_result']}")
