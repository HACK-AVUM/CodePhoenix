import os

from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv



################################################
# NON FUNZIONANTE
# NON POSSIAMO USARE AZURE PERCHE' CI LIMITA A 6 RICHIESTE AL SECONDO
# SICCOME NE FA MOLTE DI PIU' NON POSSIAMO USARLO
################################################


os.environ["AZURE_API_KEY"] = "b4436e21047b4eeab24c792dc165806c"  # "my-azure-api-key"
os.environ["AZURE_API_BASE"] = "https://openaiazuregratis.openai.azure.com"
os.environ["AZURE_API_VERSION"] = "2024-06-01"  # "2023-05-15"

llm = "azure/gpt-35-turbo"  # deployment name

os.environ['LITELLM_LOG'] = 'DEBUG'

# Funzione per analizzare il codice legacy
def analyze_code(code):
    # Define agents for legacy code analysis
    code_analyst = Agent(
        role='Legacy Code Analyst',
        goal='Analyze and understand legacy code structure and functionality',
        backstory="""You are an experienced developer with decades of experience in analyzing legacy systems.
        Your expertise lies in dissecting complex programs and understanding their core logic.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    complexity_assessor = Agent(
        role='Code Complexity Assessor',
        goal='Evaluate the overall complexity of the legacy codebase',
        backstory="""You are an expert in software metrics and complexity analysis.
        You specialize in assessing code complexity across different languages and providing actionable insights.""",
        verbose=True,
        allow_delegation=True,
        llm=llm,
    )

    # Create tasks for legacy code analysis
    task1 = Task(
        description=f"""Analyze the structure and functionality of the legacy code.
        Identify key modules, data structures, and business logic implementations.
        Code: {code}""",
        expected_output="Detailed report on code structure and functionality",
        agent=code_analyst,
    )

    task2 = Task(
        description=f"""Using the insights from the code analysis, assess the overall complexity of the legacy codebase.
        Provide metrics and recommendations for refactoring priorities.
        Code: {code}""",
        expected_output="Comprehensive complexity assessment report with refactoring suggestions",
        agent=complexity_assessor
    )

    # Instantiate the crew for legacy code analysis
    analysis_crew = Crew(
        agents=[code_analyst, complexity_assessor],
        tasks=[task1, task2],
        verbose=True,
        process=Process.sequential
    )

    # Execute the analysis
    analysis_result = analysis_crew.kickoff()

    return analysis_result


if __name__ == "__main__":
    load_dotenv()
    analysis_result = analyze_code("print('Hello world')")
    print(analysis_result)
