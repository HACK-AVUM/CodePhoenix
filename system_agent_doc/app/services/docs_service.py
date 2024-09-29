from app.services.crew_services import create_pdf_crew,create_markdown_crew,create_html_crew




def generate_pdf_documentation(model, language_to_analyze, directory_path):

    return create_pdf_crew(
        language_to_analyze=language_to_analyze,
        model=model,
        directory_path=directory_path
    )

    
