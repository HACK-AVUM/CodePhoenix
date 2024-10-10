from crewai import Crew
from crewai.process import Process

# Import TASK
from system_agent_doc.app.services.task.tasks_services import create_analyze_code_task
from system_agent_doc.app.services.task.tasks_services import create_generate_markdown_task,create_generate_html_task,create_generate_pdf_task
# Import Services
from system_agent_doc.app.services.agent.agent_services import create_code_analyzer_agent, create_html_documenter_agent, create_markdown_documenter_agent, create_pdf_documenter_agent



################## AGENT MARKDOWN CREW #####################
"""
create_markdown_crew(code) - Create a crew to analyze refactored code and generate Markdown documentation.

@:param code: str - The code to be analyzed and documented.

@:return: dict - A status message indicating success or error.
"""
def create_markdown_crew(code_refactoring_result, directory_path):


    # Create Code Analyzer Agents
    agent_code_analyze = create_code_analyzer_agent()

    # Define markdown agent generation
    agent_generation_markdown = create_markdown_documenter_agent()


    task_analyze_code = create_analyze_code_task(agent=agent_code_analyze, code_refactoring_result=code_refactoring_result)
    task_markdown_documenter = create_generate_markdown_task(agent= agent_generation_markdown,code_refactoring_result=code_refactoring_result)


    crew = Crew(
        agents=[task_analyze_code.agent, task_markdown_documenter.agent],
        tasks=[ task_analyze_code, task_markdown_documenter],
        verbose=True,
        planning=True,
        memory=True,
        process=Process.sequential
    )

    markdown_result_document = crew.kickoff(inputs={
        'directory_path': directory_path,
        'output_file':'docs/project-document.md'
    })

    return {
        "status": "success",
        "message": "Markdown documentation generated.",
        "result": markdown_result_document
    }
################## AGENT MARKDOWN CREW #####################




################## AGENT PDF CREW #####################
"""
create_markdown_crew(code) - Create a crew to analyze refactored code and generate Markdown documentation.

@:param code: str - The code to be analyzed and documented.

@:return: dict - A status message indicating success or error.
"""
def create_pdf_crew(code_refactoring_result, directory_path):



    # Create Code Analyzer Agents
    agent_code_analyze = create_code_analyzer_agent()


    # Define markdown agent generation
    agent_generation_pdf = create_pdf_documenter_agent()


    task_analyze_code = create_analyze_code_task(agent=agent_code_analyze, code_refactoring_result=code_refactoring_result)
    task_pdf_documenter = create_generate_pdf_task(agent= agent_generation_pdf, code_refactoring_result=code_refactoring_result)


    crew = Crew(
        agents=[task_analyze_code.agent, task_pdf_documenter.agent],
        tasks=[ task_analyze_code, task_pdf_documenter],
        verbose=True,
        process = Process.sequential,
    )


    pdf_result =  crew.kickoff(inputs={
        'directory_path': directory_path,
        'output_file':'docs/project-document.pdf'
    })


    print("Ecco il risultato !")

    return {
        "status": "success",
        "message": "Markdown documentation generated.",
        "result": pdf_result
    }
################## AGENT MARKDOWN CREW #####################




################## AGENT PDF CREW #####################
"""
create_markdown_crew(code) - Create a crew to analyze refactored code and generate Markdown documentation.

@:param code: str - The code to be analyzed and documented.

@:return: dict - A status message indicating success or error.
"""
def create_html_crew(code_refactoring_result, directory_path):


    # Create Code Analyzer Agents
    agent_code_analyze = create_code_analyzer_agent()

    # Define markdown agent generation
    agent_generation_html = create_html_documenter_agent()


    task_analyze_code = create_analyze_code_task(agent=agent_code_analyze, code_refactoring_result=code_refactoring_result)
    task_html_documenter = create_generate_html_task(agent= agent_generation_html, code_refactoring_result=code_refactoring_result)


    crew = Crew(
        agents=[task_analyze_code.agent, task_html_documenter.agent],
        tasks=[ task_analyze_code, task_html_documenter],
        verbose=True,
        planning=True,
        memory=True,
        process=Process.sequential
    )

    html_documentation_result = crew.kickoff(inputs={
        'directory_path': directory_path,
        'output_file':'docs/project-document.html'
    })

    return {
        "status": "success",
        "message": "Markdown documentation generated.",
        "result": html_documentation_result
    }
