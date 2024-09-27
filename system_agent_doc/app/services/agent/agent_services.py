from crewai import Agent

# Importa gli strumenti necessari
from crewai_tools import (
    
    DirectoryReadTool,
    FileReadTool,
    GithubSearchTool,
    CodeDocsSearchTool,
    CodeInterpreterTool,
    SerperDevTool,
    FileWriterTool,
)


from app.services.llm_models.models_services import get_LLM
from app.services.tools import pdf_generator_tool, html_generator_tool, markdown_generator_tool








######################################################################################## SERVICES ################################################################################



################## CREATE CODE ANALYZER AGENT #####################
"""
create_code_analyzer_agent() - create an agent for code analysis

@:param language_to_analyze - this is a language like 'JAVA' o 'Python'

@:return: an Agent instance for analyzing code
"""
def create_code_analyzer_agent(model , prompt, language_to_analyze):

    # Get Role Agent and Goal 
    role_agent ,goal_agent = get_agent_code_details(
        language_to_analyze = language_to_analyze
    ) 

    # Get type of LLM
    llm = get_LLM(model)

    return Agent(
        role= role_agent,
        goal= goal_agent,
        tools=[
            CodeInterpreterTool(),  # Analizza il codice
            DirectoryReadTool(),  # Legge directory per analisi di progetti interi
            FileReadTool(),  # Legge file specifici
            GithubSearchTool(),  # Cerca nel repository di GitHub
            CodeDocsSearchTool(),
            SerperDevTool()
        ],
        backstory= prompt,
        llm=llm,
        verbose=True
    )
####################################################



################## CREATE PDF DOCUMENT GENERATOR AGENT #####################
"""
create_pdf_documenter_agent() - create an agent for generating PDF documentation

@:return: an Agent instance for generating PDF documentation
"""
def create_pdf_documenter_agent(model, prompt):
    # Get type of LLM
    llm = get_LLM(model)
    return Agent(
        role = 'PDF Document Generator',
        goal = 'Generate documentation in PDF format.',
        tools = [
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(), 
            SerperDevTool(),
            pdf_generator_tool,
        ],
        backstory = prompt,
        llm = llm,
        verbose = True
    )
####################################################



################## CREATE MARKDOWN DOCUMENT GENERATOR AGENT #####################
"""
create_markdown_documenter_agent() - create an agent for generating Markdown documentation

@:return: an Agent instance for generating Markdown documentation
"""
def create_markdown_documenter_agent(model, prompt):
    # Get type of LLM
    llm = get_LLM(model)
    return Agent(
        role = 'Markdown Document Generator',
        goal = 'Generate documentation in Markdown format.',
        tools = [
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(), 
            SerperDevTool(),
            markdown_generator_tool, 
        ],
        backstory = prompt,
        llm = llm,
        verbose = True
    )
####################################################



################## CREATE HTML DOCUMENT GENERATOR AGENT #####################
"""
create_html_documenter_agent() - create an agent for generating HTML documentation

@:return: an Agent instance for generating HTML documentation
"""
def create_html_documenter_agent(model, prompt):
    # Get type of LLM
    llm = get_LLM(model)

    return Agent(
        role='HTML Document Generator',
        goal='Generate documentation in HTML format.',
        tools=[
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(), 
            SerperDevTool(),
            html_generator_tool, # Cerca informazioni dal database MySQL per includere dati nel HTML
        ],
        backstory=prompt,
        llm=llm,
        verbose=True
    )
####################################################






################## AGENT CODE DETAILS #####################
"""
get_agent_details(language_to_analyze) - Get the role and goal for the agent based on the specified language.

@:param language_to_analyze: str - The programming language to analyze ('JAVA' or 'Python').
@:param produce_documentation: bool - Indicate that i want a expert to produce documentantion ('JAVA' or 'Python')

@:return: tuple - A tuple containing (role_agent, goal_agent).

@:raises ValueError: If the language is unsupported.
"""
def get_agent_code_details(language_to_analyze):
    role_agent = None
    goal_agent = None

    if language_to_analyze == 'JAVA':
        role_agent = get_java_senior_expert_role()
        goal_agent = get_java_senior_expert_goal()
    elif language_to_analyze == 'Python':
        role_agent = get_python_senior_expert_role()
        goal_agent = get_python_senior_expert_goal()
    else:
        raise ValueError("Unsupported language. Please use 'JAVA' or 'Python'.")

    return role_agent, goal_agent
###############################################################



################## AGENT Documentation DETAILS #####################
"""
get_agent_documentation_details(language_to_analyze, format_documentation) - Get the role and goal for the agent based on the specified language and documentation format.

@:param language_to_analyze: str - The programming language to analyze ('JAVA' or 'Python').
@:param format_documentation: str - The format of documentation ('HTML', 'PDF', or 'MARKDOWN').

@:return: tuple - A tuple containing (role_agent, goal_agent).

@:raises ValueError: If the language or format is unsupported.
"""
def get_agent_documentation_details(language_to_analyze, format_documentation):
    role_agent = None
    goal_agent = None

    # Verifica il linguaggio e il formato della documentazione
    if language_to_analyze == 'JAVA':
        if format_documentation == 'PDF':
            role_agent = get_java_senior_documentation_pdf_agent_role()
            goal_agent = get_java_senior_documentation_pdf_agent_goal()
        elif format_documentation == 'HTML':
            role_agent = get_java_senior_documentation_html_agent_role()
            goal_agent = get_java_senior_documentation_html_agent_goal()
        elif format_documentation == 'MARKDOWN':
            role_agent = get_java_senior_documentation_markdown_agent_role()
            goal_agent = get_java_senior_documentation_markdown_agent_goal()
        else:
            raise ValueError("Unsupported documentation format. Please use 'HTML', 'PDF', or 'MARKDOWN'.")
    
    elif language_to_analyze == 'Python':
        if format_documentation == 'PDF':
            role_agent = get_python_senior_documentation_pdf_agent_role()
            goal_agent = get_python_senior_documentation_pdf_agent_goal()
        elif format_documentation == 'HTML':
            role_agent = get_python_senior_documentation_html_agent_role()
            goal_agent = get_python_senior_html_documentation_agent_goal()
        elif format_documentation == 'MARKDOWN':
            role_agent = get_python_senior_documentation_markdown_agent_role()
            goal_agent = get_python_senior_markdown_documentation_agent_goal()
        else:
            raise ValueError("Unsupported documentation format. Please use 'HTML', 'PDF', or 'MARKDOWN'.")
    
    else:
        raise ValueError("Unsupported language. Please use 'JAVA' or 'Python'.")

    return role_agent, goal_agent
##################



############################################################# ROLE JAVA AGENT ###############################################################


################## JAVA SENIOR EXPERT ROLE #####################
"""
get_java_senior_expert_role() - Get the role description for a Senior Java Expert
@:return: str - Role description for analyzing and optimizing refactored legacy code.
"""
def get_java_senior_expert_role():
    return """
    Senior Java Expert skilled in analyzing and optimizing refactored legacy code (Cobol, PL/1, JSCL, .NET) to modern Java standards.
    """
###############################################################



################## JAVA DOCUMENTATION PDF AGENT ROLE #####################
"""
get_java_senior_documentation_agent_role() - Get the role description for a Senior Java Documentation Agent
@:return: str - Role description for documenting refactored legacy code in PDF.
"""
def get_java_senior_documentation_pdf_agent_role():
    return """
    Senior Java Documentation Agent specialized in creating comprehensive PDF documentation for refactored legacy code (Cobol, PL/1, JSCL, .NET) tailored to modern Java standards.
    """
#######################################################################



################## JAVA HTML DOCUMENTATION AGENT ROLE #####################
"""
get_java_senior_html_documentation_agent_role() - Get the role description for a Senior Java HTML Documentation Agent
@:return: str - Role description for documenting refactored legacy code in HTML.
"""
def get_java_senior_documentation_html_agent_role():
    return """
    Senior Java HTML Documentation Agent focused on creating structured and accessible HTML documentation for refactored legacy code (Cobol, PL/1, JSCL, .NET) compliant with modern Java standards.
    """
#######################################################################



################## JAVA MARKDOWN DOCUMENTATION AGENT ROLE #####################
"""
get_java_senior_documentation_markdown_agent_role() - Get the role description for a Senior Java Markdown Documentation Agent
@:return: str - Role description for documenting refactored legacy code in Markdown.
"""
def get_java_senior_documentation_markdown_agent_role():
    return """
    Senior Java Markdown Documentation Agent specializing in creating concise and well-structured Markdown documentation for refactored legacy code (Cobol, PL/1, JSCL, .NET) aligned with modern Java standards.
    """
#######################################################################



############################################################# JAVA GOAL AGENT ###############################################################################################



################## JAVA SENIOR EXPERT GOAL #####################
"""
get_java_senior_expert_goal() - Get the goal description for a Senior Java Expert
@:return: str - Goal description for evaluating refactored legacy Java code.
"""
def get_java_senior_expert_goal():
    return """
    Evaluate and enhance refactored Java code from legacy systems, ensuring efficiency, maintainability, and adherence to modern Java practices.
    """
###############################################################



################## JAVA DOCUMENTATION PDF AGENT GOAL #####################
"""
get_java_senior_documentation_agent_goal() - Get the goal description for a Senior Java Documentation Agent
@:return: str - Goal description for documenting refactored legacy Java code.
"""
def get_java_senior_documentation_pdf_agent_goal():
    return """
    Generate clear and detailed PDF documentation for refactored Java code from legacy systems, ensuring clarity, accuracy, and alignment with current Java best practices.
    """
#######################################################################



################## JAVA HTML DOCUMENTATION AGENT GOAL #####################
"""
get_java_senior_html_documentation_agent_goal() - Get the goal description for a Senior Java HTML Documentation Agent
@:return: str - Goal description for documenting refactored legacy Java code.
"""
def get_java_senior_documentation_html_agent_goal():
    return """
    Produce comprehensive and user-friendly HTML documentation for refactored Java code from legacy systems, ensuring clarity, navigation ease, and alignment with current Java best practices.
    """
#######################################################################



################## JAVA MARKDOWN DOCUMENTATION AGENT GOAL #####################
"""
get_java_senior_documentation_markdown_agent_g() - Get the goal description for a Senior Java Markdown Documentation Agent
@:return: str - Goal description for documenting refactored legacy Java code.
"""
def get_java_senior_documentation_markdown_agent_goal():
    return """
    Develop clear and organized Markdown documentation for refactored Java code from legacy systems, ensuring comprehensibility, accuracy, and adherence to current Java best practices.
    """
#######################################################################



############################################################# ROLE PYTHON AGENT ##################################################################################################################



################## PYTHON SENIOR EXPERT ROLE #####################
"""
get_python_senior_expert_role() - Get the role description for a Senior Python Expert
@:return: str - Role description for analyzing and optimizing refactored legacy code.
"""
def get_python_senior_expert_role():
    return """
    Senior Python Expert experienced in analyzing and optimizing refactored legacy code (Cobol, PL/1, JSCL, .NET) to modern Python standards.
    """
###############################################################



################## PYTHON PDF DOCUMENTATION  AGENT ROLE #####################
"""
get_python_senior_documentation_agent_role() - Get the role description for a Senior Python Documentation Agent
@:return: str - Role description for documenting refactored legacy code in PDF.
"""
def get_python_senior_documentation_pdf_agent_role():
    return """
    Senior Python Documentation Agent skilled in producing thorough PDF documentation for refactored legacy code (Cobol, PL/1, JSCL, .NET) adhering to modern Python standards.
    """
#######################################################################



################## PYTHON MARKDOWN DOCUMENTATION AGENT ROLE #####################
"""
get_python_senior_markdown_documentation_agent_role() - Get the role description for a Senior Python Markdown Documentation Agent
@:return: str - Role description for documenting refactored legacy code in Markdown.
"""
def get_python_senior_documentation_markdown_agent_role():
    return """
    Senior Python Markdown Documentation Agent skilled in crafting clear and structured Markdown documentation for refactored legacy code (Cobol, PL/1, JSCL, .NET) according to modern Python standards.
    """
#######################################################################



################## PYTHON HTML DOCUMENTATION AGENT ROLE #####################
"""
get_python_senior_html_documentation_agent_role() - Get the role description for a Senior Python HTML Documentation Agent
@:return: str - Role description for documenting refactored legacy code in HTML.
"""
def get_python_senior_documentation_html_agent_role():
    return """
    Senior Python HTML Documentation Agent experienced in developing detailed and navigable HTML documentation for refactored legacy code (Cobol, PL/1, JSCL, .NET) following modern Python standards.
    """
#######################################################################



############################################################# PYTHON GOAL AGENT ###############################################################################################



################## PYTHON SENIOR EXPERT GOAL #####################
"""
get_python_senior_expert_goal() - Get the goal description for a Senior Python Expert
@:return: str - Goal description for assessing refactored legacy Python code.
"""
def get_python_senior_expert_goal():
    return """
    Assess and improve refactored Python code from legacy systems, ensuring performance, maintainability, and compliance with modern Python practices.
    """
###############################################################



################## PYTHON DOCUMENTATION PDF AGENT GOAL #####################
"""
get_python_senior_documentation_agent_goal() - Get the goal description for a Senior Python Documentation Agent
@:return: str - Goal description for documenting refactored legacy Python code.
"""
def get_python_senior_documentation_pdf_agent_goal():
    return """
    Create concise and accurate PDF documentation for refactored Python code from legacy systems, ensuring readability, correctness, and compliance with contemporary Python practices.
    """
#######################################################################



################## PYTHON HTML DOCUMENTATION AGENT GOAL #####################
"""
get_python_senior_html_documentation_agent_goal() - Get the goal description for a Senior Python HTML Documentation Agent
@:return: str - Goal description for documenting refactored legacy Python code.
"""
def get_python_senior_html_documentation_agent_goal():
    return """
    Generate clear and interactive HTML documentation for refactored Python code from legacy systems, ensuring readability, accessibility, and compliance with contemporary Python practices.
    """
#######################################################################



################## PYTHON MARKDOWN DOCUMENTATION AGENT GOAL #####################
"""
get_python_senior_markdown_documentation_agent_goal() - Get the goal description for a Senior Python Markdown Documentation Agent
@:return: str - Goal description for documenting refactored legacy Python code.
"""
def get_python_senior_markdown_documentation_agent_goal():
    return """
    Create concise and user-friendly Markdown documentation for refactored Python code from legacy systems, ensuring clarity, correctness, and compliance with contemporary Python practices.
    """
#######################################################################
