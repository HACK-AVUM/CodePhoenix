import os
from crewai import Agent, Task, Crew, Process


def perform_test(old_code, old_code_analysis_result, new_code_to_test, binary_response=False):
    # Define agents for testing
    code_tester = Agent(
        role='Code Tester',
        goal='Test and compare the functionality of old and new code',
        backstory="""You are an experienced QA engineer with expertise in testing complex systems.
        Your role is to ensure that refactored code maintains the same functionality as the original.""",
        verbose=True,
        allow_delegation=False,
        llm=os.environ["LLM"],
    )

    # Create tasks for testing
    task1 = Task(
        description=f"""Compare the functionality of the old and new code.
        Ensure that the refactored code produces the same output as the original code for various inputs.
        I forbit you from fake testing the code, but instead, just analyze the code and say if the refactored code has the same functionality as the original code or not, without any unit testing.
        Old Code: {old_code},
        Old Code Analysis Result: {old_code_analysis_result},
        New Code: {new_code_to_test}""",
        expected_output="Detailed report on functional equivalence and any discrepancies" if not binary_response else "A single binary number, 0 or 1, indicating if the refactored code has DIFFERENT functionality than the original code.",
        agent=code_tester,
    )

    # Instantiate the crew for testing
    testing_crew = Crew(
        agents=[code_tester],
        tasks=[task1],
        verbose=True,
        process=Process.sequential
    )

    # Execute the testing
    test_result = testing_crew.kickoff()

    return str(test_result.raw)
