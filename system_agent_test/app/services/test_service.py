import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv


# COMPITI
# Di nuovo, testare con codice piu complesso, incollando nel main in basso codice vecchio, relativa analisi e codice refattorizzato
# Eventualmente modificare agenti e task, o aggiungerne di nuovi, per rendere migliore e piu precisa la fase di test



os.environ["TOGETHERAI_API_KEY"] = "c47b3fa9622715d6695302a193d0488be41d61660b82ca6502eb45c61efce2c9"
llm = "together_ai/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

def perform_test(old_code, old_code_analysis_result, new_code_to_test):
    # Define agents for testing
    code_tester = Agent(
        role='Code Tester',
        goal='Test and compare the functionality of old and new code',
        backstory="""You are an experienced QA engineer with expertise in testing complex systems.
        Your role is to ensure that refactored code maintains the same functionality as the original.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    performance_analyst = Agent(
        role='Performance Analyst',
        goal='Analyze and compare the performance of old and new code',
        backstory="""You are a performance optimization expert with a keen eye for efficiency improvements.
        Your expertise lies in identifying performance bottlenecks and suggesting optimizations.""",
        verbose=True,
        allow_delegation=True,
        llm=llm,
    )

    # Create tasks for testing
    task1 = Task(
        description=f"""Compare the functionality of the old and new code.
        Ensure that the refactored code produces the same output as the original code for various inputs.
        Old Code: {old_code},
        Old Code Analysis Result: {old_code_analysis_result},
        New Code: {new_code_to_test}""",
        expected_output="Detailed report on functional equivalence and any discrepancies",
        agent=code_tester,
    )

    task2 = Task(
        description=f"""Analyze the performance characteristics of both the old and new code.
        Compare execution time, memory usage, and overall efficiency.
        Consider the complexity assessment from the analysis result.
        Old Code: {old_code},
        Old Code Analysis Result: {old_code_analysis_result},
        New Code: {new_code_to_test}""",
        expected_output="Comprehensive performance comparison report with optimization suggestions",
        agent=performance_analyst
    )

    # Instantiate the crew for testing
    testing_crew = Crew(
        agents=[code_tester, performance_analyst],
        tasks=[task1, task2],
        verbose=True,
        process=Process.sequential
    )

    # Execute the testing
    test_result = testing_crew.kickoff()

    return test_result

if __name__ == "__main__":
    load_dotenv()
    old_code = """
def calculate_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    return sum
    """
    new_code = """
def calculate_sum(numbers):
    return sum(numbers)
    """
    old_code_analysis_result = "The code is well-structured and follows best practices for readability and maintainability."
    test_result = perform_test(old_code, old_code_analysis_result, new_code)
    print(test_result)
