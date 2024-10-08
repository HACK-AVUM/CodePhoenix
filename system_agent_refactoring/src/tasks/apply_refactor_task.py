##apply_refactor_task.py: 
# Definisce il task che applica i suggerimenti di refactoring generati.
from crewai import Task
from agents.code_refactor import CodeRefactorAgent


##ApplyRefactorTask: 
# Questo task prende i suggerimenti e li applica direttamente al codice sorgente, 
# automatizzando il processo di refactoring.
class ApplyRefactorTask(Task):
    def __init__(self):
        agent = CodeRefactorAgent()
        super().__init__(
            description='Apply the suggested refactorings to the source code.',
            expected_output='Refactored code with improved readability and maintainability.',
            agent=agent
        )
