import os
from crewai import Agent


# Importa gli strumenti necessari
from crewai_tools import (
    
    DirectoryReadTool,
    FileReadTool,
    CodeDocsSearchTool,
    CodeInterpreterTool,
    SerperDevTool,
    FileWriterTool,
)


from app.services.tools import markdown_generator_tool
from app.services.tools import html_generator_tool
from app.services.tools import pdf_generator_tool


######################################################################################## SERVICES ################################################################################



################## CREATE CODE ANALYZER AGENT #####################
"""
create_code_analyzer_agent() - create an agent for code analysis

@:param language_to_analyze - this is a language like 'JAVA' o 'Python'

@:return: an Agent instance for analyzing code
"""
def create_code_analyzer_agent():

    role_agent = "Senior Code Analyzer"
    goal_agent='Analyze and understand code structure and functionality',
    backstory="""You are an experienced developer with decades of experience in analyzing and refactoring systems.
    Your expertise lies in dissecting complex programs and understanding their core logic.""",

    llm = os.environ["LLM"]

    # TODO : Modifica questi parametri e inserisci all'interno del goal il fatto di analizzare il codice di refactoring 


    return Agent(
        role = role_agent,
        goal = goal_agent,
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
def create_pdf_documenter_agent():

    role_agent = "Senior Expert Coding Documentation PDF Maker"
    role_goal = "Analyze the refactored code and generate comprehensive PDF documentation."

    backstory = """You are a senior documentation expert with extensive experience in creating detailed and professional PDF documents. 
    Your expertise lies in analyzing complex codebases, understanding the refactoring process, and presenting the information clearly and concisely in a PDF format."""

    llm = os.environ["LLM"]

    return Agent(
        role=role_agent,
        goal=role_goal,
        tools=[
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(),
            SerperDevTool(),
            pdf_generator_tool,
        ],
        backstory=backstory,
        llm=llm,
        verbose=True
    )
####################################################




################## CREATE MARKDOWN DOCUMENT GENERATOR AGENT #####################
"""
create_markdown_documenter_agent() - create an agent for generating Markdown documentation

@:return: an Agent instance for generating Markdown documentation
"""
def create_markdown_documenter_agent():

    role_agent = "Senior Expert Coding Documentation Markdown Maker"
    role_goal = "Analyze the refactored code and generate detailed Markdown documentation."

    backstory = """You are a senior documentation expert specializing in creating clear and readable Markdown documents. 
    You have a deep understanding of code analysis and refactoring processes, allowing you to produce precise and informative Markdown documentation."""

    llm = os.environ["LLM"]

    return Agent(
        role=role_agent,
        goal=role_goal,
        tools=[
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(),
            SerperDevTool(),
            markdown_generator_tool,
        ],
        backstory=backstory,
        llm=llm,
        verbose=True
    )
####################################################




################## CREATE HTML DOCUMENT GENERATOR AGENT #####################
"""
create_html_documenter_agent() - create an agent for generating HTML documentation

@:return: an Agent instance for generating HTML documentation
"""
def create_html_documenter_agent():

    role_agent = "Senior Expert Coding Documentation HTML Maker"
    role_goal = "Analyze the refactored code and generate interactive HTML documentation."

    backstory = """You are a senior documentation expert with a talent for creating dynamic and user-friendly HTML documents. 
    Your skills in analyzing refactored code and presenting it in an engaging HTML format help ensure that documentation is both informative and easy to navigate."""

    llm = os.environ["LLM"]

    return Agent(
        role=role_agent,
        goal=role_goal,
        tools=[
            DirectoryReadTool(),
            FileWriterTool(),
            FileReadTool(),
            SerperDevTool(),
            html_generator_tool,
        ],
        backstory=backstory,
        llm=llm,
        verbose=True
    )
####################################################

