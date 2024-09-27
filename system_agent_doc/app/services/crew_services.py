from crewai import Crew
from app.services.task.tasks_services import *


def start_crew(code, format):
    agents = create_agents()
    tasks = create_tasks(agents)

    analyze_code_task, generate_pdf_task, generate_markdown_task, generate_html_task = tasks

    # Select the appropriate documentation generation task
    if format == 'PDF':
        doc_task = generate_pdf_task
    elif format == 'Markdown':
        doc_task = generate_markdown_task
    elif format == 'HTML':
        doc_task = generate_html_task
    else:
        return {"error": "Unsupported format"}, 400

    crew = Crew(
        agents=[agents[0], doc_task.agent],
        tasks=[analyze_code_task, doc_task],
        verbose=True,
        planning=True
    )

    crew.kickoff()

    return {"status": "success", "message": f"Documentation generated in {format} format."}
