## refactor_crew.py
#Orchestration del processo di refactoring.
from crewai import Crew, Process
from tasks.suggest_refactor_task import SuggestRefactorTask
from tasks.apply_refactor_task import ApplyRefactorTask

##Orchestrazione: 
# Questa crew esegue prima il task di suggerimento, poi applica i refactor suggeriti in un flusso sequenziale.
# Valore: Gestisce il processo dall'analisi iniziale all'applicazione dei refactor, automatizzando il ciclo completo di refactoring.
class RefactorCrew(Crew):
    def __init__(self):
        suggest_task = SuggestRefactorTask()
        apply_task = ApplyRefactorTask()
        super().__init__(
            agents=[suggest_task.agent, apply_task.agent],
            tasks=[suggest_task, apply_task],
            process=Process.sequential
        )
