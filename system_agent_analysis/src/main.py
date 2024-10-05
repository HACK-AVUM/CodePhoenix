# src/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.code_analyzer import CodeAnalyzerAgent
from agents.report_generator import ReportGeneratorAgent
from tasks.analyze_code_task import AnalyzeCodeTask
from tasks.generate_report_task import GenerateReportTask
from crewai import Process, Crew

app = FastAPI()

# Modello Pydantic per ricevere l'input del codice
class CodeInput(BaseModel):
    project_key: str
    source_code: str

# Inizializza gli agenti e i task
code_analyzer_agent = CodeAnalyzerAgent()
report_generator_agent = ReportGeneratorAgent()

# Inizializza i task
analyze_task = AnalyzeCodeTask()
report_task = GenerateReportTask()

# Inizializza la crew che gestisce i task in sequenza
crew = Crew(
    agents=[code_analyzer_agent, report_generator_agent],
    tasks=[analyze_task, report_task],
    process=Process.sequential
)

# Endpoint per avviare l'analisi del codice
@app.post("/analyze/")
def analyze_code(input_data: CodeInput):
    try:
        result = analyze_task.run(inputs={'project_key': input_data.project_key, 'source_code': input_data.source_code})
        return {"status": "success", "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint per generare il report
@app.post("/generate-report/")
def generate_report(input_data: CodeInput):
    try:
        analysis_result = analyze_task.run(inputs={'project_key': input_data.project_key, 'source_code': input_data.source_code})
        report = report_task.run(inputs=analysis_result)
        return {"status": "success", "report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint per controllare lo stato del servizio
@app.get("/health/")
def health_check():
    return {"status": "ok"}
