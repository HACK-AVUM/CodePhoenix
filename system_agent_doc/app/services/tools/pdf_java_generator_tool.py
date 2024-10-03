import os
import subprocess
from crewai_tools import tool

@tool("DOC_JAVA_GEN")
def generate_java_python_documentation(module_path: str, output_file: str) -> str:
    """
    Genera la documentazione del codice per il file Java specificato e la salva in un file PDF.

    Args:
    - module_path (str): Il percorso del file Java di cui generare la documentazione.
    - output_file (str): Il percorso del file PDF di output.

    Returns:
    - str: Percorso del file PDF generato.
    """
    # Crea la cartella di output se non esiste
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Genera la documentazione HTML utilizzando javadoc
    output_dir = os.path.splitext(output_file)[0] + "_html"
    command = f"javadoc -d {output_dir} {module_path}"
    subprocess.run(command, shell=True, check=True)

    # Converti la documentazione HTML in PDF (puoi usare un convertitore HTML-PDF come wkhtmltopdf)
    pdf_command = f"wkhtmltopdf {output_dir}/index.html {output_file}"
    subprocess.run(pdf_command, shell=True, check=True)

    return output_file