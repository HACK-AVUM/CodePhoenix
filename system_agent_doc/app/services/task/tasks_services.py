from crewai import Task


################## CREATE ANALYZE CODE TASK #####################
"""
create_analyze_code_task() - create a task for analyzing refactored code
@:parameter agent - Agent instance for code analysis
@:return: a Task instance for analyzing refactored code
"""
def create_analyze_code_task(agent):
    return Task(
        description='Perform a comprehensive analysis of the refactored code written in Python and Java. Identify improvements, potential issues, and adherence to best practices.',
        expected_output='A detailed report outlining the analysis of the refactored code, including identified issues, areas of improvement, and adherence to coding standards.',
        agent=agent
    )
####################################################

################## CREATE PDF DOCUMENTATION TASK #####################
"""
create_generate_pdf_task() - create a task for generating PDF documentation
@:parameter agent - Agent instance for PDF documentation generation
@:return: a Task instance for generating PDF documentation
"""
def create_generate_pdf_task(agent):
    return Task(
        description='Generate comprehensive PDF documentation based on the code analysis report. Ensure the documentation is well-structured and includes all necessary details.',
        expected_output='A well-structured PDF document containing detailed documentation of the code, including analysis results, code snippets, and explanations.',
        agent=agent
    )
####################################################

################## CREATE MARKDOWN DOCUMENTATION TASK #####################
"""
create_generate_markdown_task() - create a task for generating Markdown documentation
@:parameter agent - Agent instance for Markdown documentation generation
@:return: a Task instance for generating Markdown documentation
"""
def create_generate_markdown_task(agent):
    return Task(
        description='Generate comprehensive Markdown documentation based on the code analysis report. Ensure the documentation is well-structured and includes all necessary details.',
        expected_output='A well-structured Markdown document containing detailed documentation of the code, including analysis results, code snippets, and explanations.',
        agent=agent
    )
####################################################

################## CREATE HTML DOCUMENTATION TASK #####################
"""
create_generate_html_task() - create a task for generating HTML documentation
@:parameter agent - Agent instance for HTML documentation generation
@:return: a Task instance for generating HTML documentation
"""
def create_generate_html_task(agent):
    return Task(
        description='Generate comprehensive HTML documentation based on the code analysis report. Ensure the documentation is well-structured and includes all necessary details, formatted appropriately for web viewing.',
        expected_output='A well-structured HTML document containing detailed documentation of the code, including analysis results, code snippets, and explanations, formatted for web viewing.',
        agent=agent,
    )
####################################################
