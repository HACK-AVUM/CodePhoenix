from crewai import Crew
# Import TASK 
from app.services.task.tasks_services import create_analyze_code_task
from app.services.task.tasks_services import create_generate_markdown_task,create_generate_html_task,create_generate_pdf_task
# Import Services 
from app.services.agent.agent_services import create_code_analyzer_agent, create_html_documenter_agent, create_markdown_documenter_agent, create_pdf_documenter_agent


################## AGENT MARKDOWN CREW #####################
"""
create_markdown_crew(code) - Create a crew to analyze refactored code and generate Markdown documentation.

@:param code: str - The code to be analyzed and documented.

@:return: dict - A status message indicating success or error.
"""
def create_markdown_crew(model , prompt , language_to_analyze):
    
    
    # Create Code Analyzer Agents
    agent_code_analyze = create_code_analyzer_agent(
        model= model,
        prompt=prompt,
        language_to_analyze=language_to_analyze
    )

    # Define markdown agent generation 
    agent_generation_markdown = create_markdown_documenter_agent(
        model=model,
        prompt=prompt
    )


    task_analyze_code = create_analyze_code_task(agent=agent_code_analyze)
    task_markdown_documenter = create_generate_markdown_task(agent= agent_generation_markdown)


    crew = Crew(
        agents=[task_analyze_code.agent, task_markdown_documenter.agent],
        tasks=[ task_analyze_code, task_markdown_documenter],
        verbose=True,
        planning=True
    )

    crew.kickoff()

    return {"status": "success", "message": "Markdown documentation generated."}
################## AGENT MARKDOWN CREW #####################

