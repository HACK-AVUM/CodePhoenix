import os

from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

os.environ["TOGETHERAI_API_KEY"] = "c47b3fa9622715d6695302a193d0488be41d61660b82ca6502eb45c61efce2c9"
llm = "together_ai/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"


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
        allow_delegation=False,
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

    return str(analysis_result.raw)


if __name__ == "__main__":
    load_dotenv()
    analysis_result = analyze_code("print('Hello world')")
    print(analysis_result)