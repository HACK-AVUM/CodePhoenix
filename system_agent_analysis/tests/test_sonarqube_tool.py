## test_sonarqube_tool.py
# Questo test verifica il corretto funzionamento del tool di SonarQube, 
# assicurando che possa inviare codice all'API di SonarQube e ricevere un output.

import unittest
from src.tools.sonarqube_tool import SonarQubeTool
from unittest.mock import patch

##Test del tool di SonarQube: 
# Simuliamo l'invio di codice all'API di SonarQube usando unittest.mock per controllare la risposta dell'API.
class TestSonarQubeTool(unittest.TestCase):
    @patch('tools.sonarqube_tool.requests.post')
    def test_analyze_code(self, mock_post):
        # Simuliamo una risposta positiva dall'API di SonarQube
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            'issues': [
                {'severity': 'Critical', 'message': 'Null pointer dereference'},
                {'severity': 'Major', 'message': 'Unused import statement'}
            ]
        }
        
        tool = SonarQubeTool(sonar_url='https://sonarqube.example.com', sonar_token='dummy_token')
        result = tool.analyze_code('my_project', 'sample_code')
        
        ##Verifica dei risultati: Il test verifica che la chiamata all'API di SonarQube restituisca dati strutturati correttamente, come una lista di problemi di codice.
        self.assertIsNotNone(result)
        self.assertEqual(result['issues'][0]['severity'], 'Critical')
        self.assertEqual(result['issues'][1]['message'], 'Unused import statement')

if __name__ == '__main__':
    unittest.main()
