import pydoc
from crewai_tools import tool

@tool
def generate_html_documentation(module_name: str, output_file: str) -> str:
    """
    Genera la documentazione del codice per il modulo specificato e la salva in un file HTML.

    Args:
        module_name (str): Il nome del modulo di cui generare la documentazione.
        output_file (str): Il percorso del file HTML di output.

    Returns:
        str: Percorso del file HTML generato.
    """
    # Genera la documentazione del modulo come stringa in HTML
    documentation = pydoc.html.document(module_name)

    # Salva la documentazione in un file HTML
    with open(output_file, 'w') as file:
        file.write(documentation)

    return output_file