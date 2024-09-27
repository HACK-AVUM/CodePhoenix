from crewai_tools import tool
import pydoc
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

@tool
def generate_pdf_documentation(module_name: str, output_file: str) -> str:
    """
    Genera la documentazione del codice per il modulo specificato e la salva in un file PDF.

    Args:
    - module_name (str): Il nome del modulo di cui generare la documentazione.
    - output_file (str): Il percorso del file PDF di output.

    Returns:
    - str: Percorso del file PDF generato.
    """
    # Genera la documentazione del modulo come stringa
    documentation = pydoc.render_doc(module_name, renderer=pydoc.plaintext)

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