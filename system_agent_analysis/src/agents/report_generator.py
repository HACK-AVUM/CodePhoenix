## report_generator.py
#Questo agente è responsabile della generazione del report finale, utilizzando il FormattingTool per strutturare i risultati dell'analisi in un formato leggibile.
from crewai import Agent
from tools.formatting_tool import FormattingTool

##Descrizione dell'agente: Il ReportGeneratorAgent è responsabile della creazione del report basato sui dati dell'analisi del codice. 
# Utilizza il FormattingTool per generare un report in markdown o HTML.
class ReportGeneratorAgent(Agent):
    def __init__(self):
        formatting_tool = FormattingTool(format_type='markdown')
        super().__init__(
            role='Report Generator',
            goal='Compile a detailed report based on the code analysis results.',
            tools=[formatting_tool],
            verbose=True,
            allow_delegation=True
        )
    

    ##Metodo generate_report: 
    # Questo metodo viene usato per chiamare il tool di formattazione e creare il report finale.
    # Valore: Con il formato markdown predefinito, il report è facilmente leggibile dai team tecnici e integrabile in sistemi di documentazione o dashboard di monitoraggio.
    def generate_report(self, analysis_data):
        return self.tools[0].format_report(analysis_data)
