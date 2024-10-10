from system_agent_doc.app.services.crew_services import create_pdf_crew,create_markdown_crew,create_html_crew




def generate_pdf_documentation(code_refactoring_result, directory_path):

    return create_pdf_crew(code_refactoring_result=code_refactoring_result,directory_path=directory_path)



def generate_html_documentation(code_refactoring_result, directory_path):
        
    return create_html_crew(code_refactoring_result=code_refactoring_result,directory_path=directory_path)


def generate_markdown_documentation(code_refactoring_result, directory_path):
    return create_markdown_crew(code_refactoring_result=code_refactoring_result,directory_path=directory_path)