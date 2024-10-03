from crewai import Agent

from app.services.agent.agent_java import *
from app.services.agent.agent_python import *

# Importa gli strumenti necessari
from crewai_tools import (
    
    DirectoryReadTool,
    FileReadTool,
    CodeDocsSearchTool,
    CodeInterpreterTool,
    SerperDevTool,
    FileWriterTool,
)


from app.services.agent.agent_python import get_python_html_documentation_agent_backstory, get_python_markdown_documentation_agent_backstory, get_python_pdf_documentation_agent_backstory, get_python_senior_documentation_html_agent_role, get_python_senior_documentation_markdown_agent_role, get_python_senior_documentation_pdf_agent_goal, get_python_senior_documentation_pdf_agent_role, get_python_senior_expert_backstory, get_python_senior_expert_goal, get_python_senior_expert_role, get_python_senior_html_documentation_agent_goal, get_python_senior_markdown_documentation_agent_goal
from app.services.llm_models.models_services import get_LLM
from app.services.tools import markdown_generator_tool
from app.services.tools import html_generator_tool
from app.services.tools.pdf_java_generator_tool import generate_java_python_documentation
from app.services.tools.pdf_python__generator_tool import generate_pdf_python_documentation

define_markdown_symbol="MARKDOWN"
define_pdf_symbol="PDF"
define_html_symbol="HTML"




######################################################################################## SERVICES ################################################################################



################## CREATE CODE ANALYZER AGENT #####################
"""
create_code_analyzer_agent() - create an agent for code analysis

@:param language_to_analyze - this is a language like 'JAVA' o 'Python'

@:return: an Agent instance for analyzing code
"""
def create_code_analyzer_agent(model , language_to_analyze):

    # Get Role Agent and Goal 
    role_agent ,goal_agent, backstory = get_agent_code_details(
        language_to_analyze = language_to_analyze
    ) 

    # Get type of LLM
    llm = get_LLM(model)

    return Agent(
        role= role_agent,
        goal= goal_agent,
        tools=[
            CodeInterpreterTool(),  
            DirectoryReadTool(),  
            FileReadTool(),  
            CodeDocsSearchTool(),
            SerperDevTool(),
            
        ],
        backstory= backstory ,
        llm=llm,
        verbose=True
    )
####################################################



################## CREATE PDF DOCUMENT GENERATOR AGENT #####################
"""
create_pdf_documenter_agent() - create an agent for generating PDF documentation

@:return: an Agent instance for generating PDF documentation
"""
def create_pdf_documenter_agent(model, language_to_analyze):

    # Get type of LLM
    llm = get_LLM(model)

    role_agent, role_goal , backstory = get_agent_documentation_details(
        language_to_analyze=language_to_analyze,
        format_documentation=define_pdf_symbol
    )

    


    tool_pdf_gen = None
    if language_to_analyze == 'JAVA' :

        tool_pdf_gen = generate_java_python_documentation
    else:

        tool_pdf_gen = generate_pdf_python_documentation

    print("Sono qui! per poter instanziare l'agente PDF")

    return Agent(

        role = role_agent,
        goal = role_goal,
        
        tools = [
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(), 
            SerperDevTool(),
            tool_pdf_gen,
        ],
        backstory=backstory,
        llm = llm,
        verbose = True
    )
####################################################



################## CREATE MARKDOWN DOCUMENT GENERATOR AGENT #####################
"""
create_markdown_documenter_agent() - create an agent for generating Markdown documentation

@:return: an Agent instance for generating Markdown documentation
"""
def create_markdown_documenter_agent(model, language_to_analyze):
    # Get type of LLM
    llm = get_LLM(model)

    role_agent, role_goal, backstory = get_agent_documentation_details(
        language_to_analyze=language_to_analyze,
        format_documentation=define_markdown_symbol
    )

    return Agent(
        role = role_agent,
        goal = role_goal,
        tools = [
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(), 
            SerperDevTool(),
            markdown_generator_tool, 
        ],
        backstory = backstory,
        llm = llm,
        verbose = True
    )
####################################################



################## CREATE HTML DOCUMENT GENERATOR AGENT #####################
"""
create_html_documenter_agent() - create an agent for generating HTML documentation

@:return: an Agent instance for generating HTML documentation
"""
def create_html_documenter_agent(model, language_to_analyze):
    # Get type of LLM
    llm = get_LLM(model)
    role_agent, role_goal , backstory = get_agent_documentation_details(
        language_to_analyze=language_to_analyze,
        format_documentation=define_markdown_symbol
    )



    return Agent(
        role= role_agent,
        goal= role_goal,
        tools=[
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(), 
            SerperDevTool(),
            html_generator_tool, # Cerca informazioni dal database MySQL per includere dati nel HTML
        ],
        backstory=backstory,
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
    backstory_agent = None

    if language_to_analyze == 'JAVA':
        role_agent = get_java_senior_expert_role()
        goal_agent = get_java_senior_expert_goal()
        backstory_agent = get_java_senior_expert_backstory()
    elif language_to_analyze == 'Python':
        role_agent = get_python_senior_expert_role()
        goal_agent = get_python_senior_expert_goal()
        backstory_agent = get_python_senior_expert_backstory()
    else:
        raise ValueError("Unsupported language. Please use 'JAVA' or 'Python'.")

    return role_agent, goal_agent, backstory_agent
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
    backstory_agent = None

    # Verifica il linguaggio e il formato della documentazione
    if language_to_analyze == 'JAVA':
        if format_documentation == 'PDF':
            role_agent = get_java_senior_documentation_pdf_agent_role()
            goal_agent = get_java_senior_documentation_pdf_agent_goal()
            backstory_agent = get_java_senior_expert_backstory()
        elif format_documentation == 'HTML':
            role_agent = get_java_senior_documentation_html_agent_role()
            goal_agent = get_java_senior_documentation_html_agent_goal()
            backstory_agent = get_java_senior_expert_backstory() 
        elif format_documentation == 'MARKDOWN':
            role_agent = get_java_senior_documentation_markdown_agent_role()
            goal_agent = get_java_senior_documentation_markdown_agent_goal()
            backstory_agent = get_java_senior_expert_backstory()
        else:
            raise ValueError("Unsupported documentation format. Please use 'HTML', 'PDF', or 'MARKDOWN'.")
        
    
    elif language_to_analyze == 'Python':
        if format_documentation == 'PDF':
            role_agent = get_python_senior_documentation_pdf_agent_role()
            goal_agent = get_python_senior_documentation_pdf_agent_goal()
            backstory_agent = get_python_pdf_documentation_agent_backstory()
            

        elif format_documentation == 'HTML':
            role_agent = get_python_senior_documentation_html_agent_role()
            goal_agent = get_python_senior_html_documentation_agent_goal()
            backstory_agent = get_python_html_documentation_agent_backstory() 
        
        elif format_documentation == 'MARKDOWN':
            role_agent = get_python_senior_documentation_markdown_agent_role()
            goal_agent = get_python_senior_markdown_documentation_agent_goal()
            backstory_agent = get_python_markdown_documentation_agent_backstory()
        else:
            raise ValueError("Unsupported documentation format. Please use 'HTML', 'PDF', or 'MARKDOWN'.")
    
    else:
        raise ValueError("Unsupported language. Please use 'JAVA' or 'Python'.")

    return role_agent, goal_agent, backstory_agent
###############################################################################