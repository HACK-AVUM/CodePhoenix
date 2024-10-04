## quality_control_crew.py
# Definisce il processo che combina i task di analisi del codice e generazione del report in un flusso di lavoro sequenziale o parallelo.

from crewai import Crew, Process
from tasks.analyze_code_task import AnalyzeCodeTask
from tasks.generate_report_task import GenerateReportTask


##Descrizione del Crew: 
# Questa crew è responsabile della gestione di più agenti e task, eseguendo prima l'analisi del codice e poi la generazione del report.
class QualityControlCrew(Crew):
    def __init__(self):
        analyze_task = AnalyzeCodeTask()
        report_task = GenerateReportTask()
        super().__init__(
            agents=[analyze_task.agent, report_task.agent],
            tasks=[analyze_task, report_task],

            ##Processo: 
            # Utilizza Process.sequential, il che significa che i task verranno eseguiti uno dopo l'altro, 
            # garantendo che il report venga generato solo dopo il completamento dell'analisi.
            process=Process.sequential
        )
