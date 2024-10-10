import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv



load_dotenv()


def analyze_code(code, number_response=False):
    
    code_analyst = Agent(
        role='Legacy Code Analyst',
        goal='Analyze and understand legacy code structure and functionality',
        backstory="""You are an experienced developer with decades of experience in analyzing legacy systems.
        Your expertise lies in dissecting complex programs and understanding their core logic.""",
        verbose=True,
        allow_delegation=False,
        llm=os.environ["LLM"],
    )

    complexity_assessor = Agent(
        role='Code Complexity Assessor',
        goal='Evaluate the overall complexity of the legacy codebase',
        backstory="""You are an expert in software metrics and complexity analysis.
        You specialize in assessing code complexity across different languages and providing actionable insights.""",
        verbose=True,
        allow_delegation=False,
        llm=os.environ["LLM"],
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
        expected_output="Comprehensive complexity assessment report with refactoring suggestions" if not number_response else "A single digit number, from 0 to 9 inclusive, indicating the complexity of the code.",
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

