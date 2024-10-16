##analyze_code_task.py:
# Definisce il task che assegna all'agente di analisi del codice il compito di elaborare il codice sorgente.

from crewai import Task
from ..code_analyzer import CodeAnalyzerAgent

class AnalyzeCodeTask(Task):
    def __init__(self):
        agent = CodeAnalyzerAgent()
        super().__init__(
            description='Analyze source code using SonarQube and report issues.',
            expected_output='Code quality report with identified issues.',
            agent=agent
        )
