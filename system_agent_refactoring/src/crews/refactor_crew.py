import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv


# COMPITI
# Di nuovo, testare con codice piu complesso, incollando nel main in basso codice e relativo output del microservizio di analisi
# Eventualmente modificare agenti e task, o aggiungerne di nuovi, per rendere migliore il refactoring



os.environ["TOGETHERAI_API_KEY"] = "c47b3fa9622715d6695302a193d0488be41d61660b82ca6502eb45c61efce2c9"
llm = "together_ai/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

def refactoring_code(code, analysis_result):
    # Define agents for code refactoring
    code_analyzer = Agent(
        role='Code Analyzer',
        goal='Analyze and understand code structure and functionality',
        backstory="""You are an experienced developer with decades of experience in analyzing and refactoring systems.
        Your expertise lies in dissecting complex programs and understanding their core logic.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    refactoring_expert = Agent(
        role='Refactoring Expert',
        goal='Refactor the code to improve its structure and readability',
        backstory="""You are an expert in software refactoring techniques.
        You specialize in improving code quality, reducing complexity, and enhancing maintainability.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
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

if __name__ == "__main__":
    load_dotenv()
    sample_code = """
def calculate_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    return sum
    """

    analysis_result = "The code is well-structured and follows best practices for readability and maintainability."
    refactoring_result = refactoring_code(sample_code, analysis_result)
    print(refactoring_result)