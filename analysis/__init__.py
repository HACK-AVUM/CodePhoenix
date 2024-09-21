import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()

os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key

with open('test.cob', 'r') as file:
    cobol_code = file.read()


# Define agents for legacy code analysis
cobol_analyst = Agent(
    role='COBOL Code Analyst',
    goal='Analyze and understand COBOL legacy code structure and functionality',
    backstory="""You are an experienced COBOL developer with decades of experience in mainframe systems.
    Your expertise lies in dissecting complex COBOL programs and understanding their core logic.""",
    verbose=True,
    allow_delegation=False,
)

jcl_analyst = Agent(
    role='JCL Specialist',
    goal='Examine JCL scripts and their interaction with COBOL programs',
    backstory="""You are a JCL expert with in-depth knowledge of mainframe job control.
    You excel at understanding how JCL scripts orchestrate the execution of COBOL programs.""",
    verbose=True,
    allow_delegation=False,
)

pli_analyst = Agent(
    role='PL/I Code Analyst',
    goal='Analyze PL/I code structure and its integration with COBOL systems',
    backstory="""You are a seasoned PL/I developer with a strong background in mainframe applications.
    Your strength is in understanding complex PL/I code and its interaction with COBOL programs.""",
    verbose=True,
    allow_delegation=False,
)

complexity_assessor = Agent(
    role='Code Complexity Assessor',
    goal='Evaluate the overall complexity of the legacy codebase',
    backstory="""You are an expert in software metrics and complexity analysis.
    You specialize in assessing code complexity across different languages and providing actionable insights.""",
    verbose=True,
    allow_delegation=True
)

# Create tasks for legacy code analysis
task1 = Task(
    description=f"""Analyze the structure and functionality of the COBOL code.
    Identify key modules, data structures, and business logic implementations.
    Cobol code: {cobol_code}""",
    expected_output="Detailed report on COBOL code structure and functionality",
    agent=cobol_analyst
)

task2 = Task(
    description="""Examine the JCL scripts associated with the COBOL programs.
    Determine job steps, data flow, and integration points.""",
    expected_output="Comprehensive analysis of JCL scripts and their role in the system",
    agent=jcl_analyst
)

task3 = Task(
    description="""Analyze the PL/I code components and their interaction with COBOL programs.
    Identify shared data structures and inter-program communication.""",
    expected_output="Detailed report on PL/I code structure and COBOL integration",
    agent=pli_analyst
)

task4 = Task(
    description=f"""Using the insights from previous analyses, assess the overall complexity of the legacy codebase.
    Provide metrics and recommendations for refactoring priorities.
    Cobol code: {cobol_code}""",
    expected_output="Comprehensive complexity assessment report with refactoring suggestions",
    agent=complexity_assessor
)

# Instantiate the crew for legacy code analysis
analysis_crew = Crew(
    agents=[cobol_analyst, jcl_analyst, pli_analyst, complexity_assessor],
    tasks=[task1, task2, task3, task4],
    verbose=True,
    process=Process.sequential
)

# Execute the analysis

analysis_result = analysis_crew.kickoff()

print("######################")
print(analysis_result)
