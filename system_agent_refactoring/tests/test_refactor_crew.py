## test_refactor_crew.py
#Questo test verifica che la crew funzioni come previsto, eseguendo i task sequenziali di suggerimento e applicazione dei refactor.

import unittest
from src.crews.refactor_crew import RefactorCrew

class TestRefactorCrew(unittest.TestCase):
    def test_crew_execution(self):
        ## Simulazione dell'input di codice: 
        # Qui passiamo un codice di esempio con problemi come funzioni troppo lunghe e duplicati.
        code_data = {
            'functions': 15,
            'duplicate_code': True,
            'source_code': 'def my_func(): pass'
        }
        
        #Inizializzazione della Crew: 
        # Viene creata un'istanza della RefactorCrew che orchestrerà i task.
        crew = RefactorCrew()

        #Esecuzione della Crew: 
        # Chiamiamo il metodo kickoff() della crew per avviare i task in sequenza.
        result = crew.kickoff(inputs={'code_data': code_data})
        
        ##Verifiche: 
        # Verifichiamo che il risultato dell'esecuzione contenga i suggerimenti di refactoring e che il refactoring sia stato applicato al codice.
        self.assertIn("Suggestions for refactoring", result)
        self.assertIn("Refactored code", result)

if __name__ == '__main__':
    unittest.main()
