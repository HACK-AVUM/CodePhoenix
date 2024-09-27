from crewai_tools import tool
import pydoc
import markdown2

@tool
def generate_markdown_documentation(module_name: str, output_file: str) -> str:
    """
    Genera la documentazione del codice per il modulo specificato e la salva in un file Markdown.

    Args:
    - module_name (str): Il nome del modulo di cui generare la documentazione.
    - output_file (str): Il percorso del file Markdown di output.

    Returns:
    - str: Percorso del file Markdown generato.
    """
    # Genera la documentazione del modulo come stringa
    documentation = pydoc.render_doc(module_name, renderer=pydoc.plaintext)
    
    # Converti la documentazione in formato Markdown
    markdown_content = markdown2.markdown(documentation)
    
    # Scrivi la documentazione Markdown nel file di output
    with open(output_file, 'w') as file:
        file.write(markdown_content)
    
    return output_file