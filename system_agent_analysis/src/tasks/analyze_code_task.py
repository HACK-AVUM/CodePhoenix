from crewai import Task
from agents.code_analyzer import CodeAnalyzerAgent

class AnalyzeCodeTask(Task):
    def __init__(self):
        agent = CodeAnalyzerAgent()
        super().__init__(
            description='Analyze source code using SonarQube and report issues.',
            expected_output='Code quality report with identified issues.',
            agent=agent
        )
