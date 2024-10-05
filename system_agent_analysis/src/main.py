## FastAPI è stato configurato per gestire l'endpoint /analyze/. 
# L'utente invierà il codice da analizzare come stringa al microservizio.from fastapi import FastAPI
from fastapi import FastAPI
import subprocess

app = FastAPI()

# Endpoint per avviare l'analisi del codice
@app.post("/analyze/")
def analyze_code(code: str):
    """
    Funzione per eseguire l'analisi del codice con SonarScanner.
    """
    # Simula l'analisi del codice con SonarScanner
    # Qui possiamo usare subprocess per chiamare sonar-scanner
    ##SonarScanner: 
    # Usiamo subprocess.run() per chiamare SonarScanner e avviare l'analisi del codice
    command = ['sonar-scanner', '-Dsonar.projectKey=my_project', '-Dsonar.sources=src']
    subprocess.run(command, check=True)
    
    return {"result": "Analysis complete"}
