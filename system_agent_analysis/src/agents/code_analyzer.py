##code_analyzer.py: 
# Definisce l'agente che esegue l'analisi del codice utilizzando SonarQube.
from crewai import Agent
from ..tools.sonarqube_tool import SonarQubeTool


class CodeAnalyzerAgent(Agent):
    def __init__(self):
        sonar_tool = SonarQubeTool(sonar_url='http://localhost:9000/dashboard?id=Hackaton-System-Multi-Agent', sonar_token='48c1b978-0271-4977-8f93-06e165fc7f0f')
        super().__init__(
            role='Code Analyzer',
            goal='Analyze source code using SonarQube',
            tools=[sonar_tool],
            verbose=True,
            allow_delegation=False,
        )
