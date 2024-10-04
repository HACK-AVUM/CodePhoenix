## test_quality_control_crew.py
#Questa classe di test si assicura che il flusso della crew funzioni correttamente dall'inizio alla fine.
import unittest
from src.crews.quality_control_crew import QualityControlCrew


##Test dell'intera Crew: 
# Questo test simula l'intera esecuzione della crew, dall'analisi del codice alla generazione del report.
class TestQualityControlCrew(unittest.TestCase):
    def test_crew_execution(self):
        crew = QualityControlCrew()

        ##Metodo kickoff: 
        # Verifica che il flusso funzioni correttamente e che l'output contenga il report finale.
        result = crew.kickoff(inputs={'project_key': 'my_project', 'source_code': 'sample_code'})
        self.assertIn('Code Quality Report', result)

if __name__ == '__main__':
    unittest.main()
