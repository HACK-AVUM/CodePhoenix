##suggest_refactor_task.py: 
# Definisce il task che assegna all'agente il compito di identificare suggerimenti di refactoring.
from crewai import Task
from agents.code_refactor import CodeRefactorAgent


##SuggestRefactorTask: 
# Il task di suggerimento analizza il codice e fornisce raccomandazioni, come eliminare duplicazioni, 
# rinominare variabili o separare funzioni lunghe in funzioni più piccole.
class SuggestRefactorTask(Task):
    def __init__(self):
        agent = CodeRefactorAgent()
        super().__init__(
            description='Analyze the source code and suggest improvements based on refactoring best practices.',
            expected_output='Suggestions for refactoring the code to improve readability, maintainability, and performance.',
            agent=agent
        )
