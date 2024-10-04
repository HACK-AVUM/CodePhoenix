## generate_report_task.py
#Questa classe gestisce il task assegnato all'agente di reportistica, 
#che prende i risultati dell'analisi del codice e genera un report ben strutturato e leggibile.
from crewai import Task
from agents.report_generator import ReportGeneratorAgent

class GenerateReportTask(Task):
    def __init__(self):

        ##Agente assegnato: 
        # Il task viene eseguito dal ReportGeneratorAgent, 
        # che si occupa della formattazione e della sintesi dei dati.
        agent = ReportGeneratorAgent()
        super().__init__(

            ##Descrizione del task: Questo task è responsabile della trasformazione dei dati grezzi ricevuti da SonarQube in un report leggibile.
            description='Generate a detailed report based on the code analysis results from SonarQube.',

            ##Expected Output: 
            #L'output atteso è un report ben strutturato che evidenzia i problemi principali rilevati nel codice. 
            # Questo potrebbe includere vulnerabilità di sicurezza, bug, code smells, ecc.
            expected_output='A well-structured report summarizing key issues found in the codebase.',
            agent=agent
        )

##Ragionamento: 
# Separare il task di generazione del report rende il flusso di lavoro più modulare e organizzato. 
# Questo approccio permette di espandere facilmente la capacità di generare diversi tipi di report (ad esempio, PDF, HTML) senza influire sulla logica dell'analisi del codice