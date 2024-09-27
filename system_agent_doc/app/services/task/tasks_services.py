from crewai import Task

################## CREATE ANALYZE CODE TASK #####################
"""
create_analyze_code_task() - create a task for analyzing refactored code
@:parameter agent - Agent instance for code analysis
@:return: a Task instance for analyzing refactored code
"""
def create_analyze_code_task(agent):
    return Task(
        description='Analyze the refactored code written in Python and Java.',
        expected_output='Detailed analysis report of the refactored code.',
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
        description='Generate PDF documentation based on the code analysis report.',
        expected_output='PDF document with detailed code documentation.',
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
        description='Generate Markdown documentation based on the code analysis report.',
        expected_output='Markdown document with detailed code documentation.',
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
        description='Generate HTML documentation based on the code analysis report.',
        expected_output='HTML document with detailed code documentation.',
        agent=agent
    )
####################################################
