# src/main.py
from fastapi import FastAPI
import subprocess

app = FastAPI()

# Endpoint per avviare il refactoring del codice
@app.post("/refactor/")
def refactor_code(code: str):
    """
    Funzione per applicare refactoring al codice e inviare l'analisi del codice refattorizzato a SonarQube.
    """
    # Qui potresti avere una logica per refattorizzare il codice
    refactored_code = code  # Refattorizza il codice qui (es. eliminazione di duplicati)

    # Esegui sonar-scanner per analizzare il codice refattorizzato
    command = ['sonar-scanner', '-Dsonar.projectKey=my_project', '-Dsonar.sources=src']
    subprocess.run(command, check=True)

    return {"result": "Refactoring and analysis complete"}
