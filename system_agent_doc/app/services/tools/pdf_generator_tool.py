from crewai_tools import tool
import pydoc
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import os


@tool("PDF-DOC")
def generate_pdf(module_path: str, output_file: str) -> str:
    """
    Genera la documentazione del codice per il file Python specificato e la salva in un file PDF.

    Args:
    - module_path (str): Il percorso del file di cui generare la documentazione.
    - output_file (str): Il percorso del file PDF di output.

    Returns:
    - str: Percorso del file PDF generato.
    """
    # Ottieni il nome del modulo dal percorso del file
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    
    # Genera la documentazione del modulo come stringa
    documentation = pydoc.render_doc(module_name, renderer=pydoc.plaintext)

    # Crea la cartella di output se non esiste
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Crea un canvas per il PDF
    pdf_canvas = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Imposta la posizione iniziale
    y_position = height - 40

    # Aggiungi la documentazione al PDF
    for line in documentation.split('\n'):
        if y_position < 40:
            pdf_canvas.showPage()
            y_position = height - 40
        pdf_canvas.drawString(40, y_position, line)
        y_position -= 14

    # Salva il PDF
    pdf_canvas.save()

    return output_file


