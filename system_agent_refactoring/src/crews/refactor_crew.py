import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv



def refactoring_code(code, analysis_result):
    # Define agents for code refactoring
    code_analyzer = Agent(
        role='Code Analyzer',
        goal='Analyze and understand code structure and functionality',
        backstory="""You are an experienced developer with decades of experience in analyzing and refactoring systems.
        Your expertise lies in dissecting complex programs and understanding their core logic.""",
        verbose=True,
        allow_delegation=False,
        llm=os.environ["LLM"],
    )

    refactoring_expert = Agent(
        role='Refactoring Expert',
        goal='Refactor the code to improve its structure and readability',
        backstory="""You are an expert in software refactoring techniques.
        You specialize in improving code quality, reducing complexity, and enhancing maintainability.""",
        verbose=True,
        allow_delegation=False,
        llm=os.environ["LLM"],
    )

    # Create tasks for code refactoring
    task1 = Task(
        description=f"""Analyze the structure and functionality of the given code.
        Identify areas that need improvement in terms of design, efficiency, and readability.
        Code: {code}
        Analysis Result: {analysis_result}""",
        expected_output="Detailed report on code structure and areas for improvement",
        agent=code_analyzer,
    )

    task2 = Task(
        description=f"""Using the insights from the code analysis, refactor the code to improve its quality.
        Focus on enhancing readability, reducing complexity, and applying best practices.
        Code: {code}
        Analysis Result: {analysis_result}""",
        expected_output="Refactored code with explanations of improvements made",
        agent=refactoring_expert
    )

    # Instantiate the crew for code refactoring
    refactoring_crew = Crew(
        agents=[code_analyzer, refactoring_expert],
        tasks=[task1, task2],
        verbose=True,
        process=Process.sequential
    )

    # Execute the refactoring
    refactoring_result = refactoring_crew.kickoff()

    return str(refactoring_result.raw)

