## test_report_generator.py: 
# Questo test verifica che l'agente di reportistica (ReportGeneratorAgent) funzioni correttamente 
# e generi un report formattato in base ai dati forniti.

import unittest
from src.agents.report_generator import ReportGeneratorAgent
from src.tools.formatting_tool import FormattingTool

##Test dell'agente di reportistica: 
# Questo test crea un'istanza di ReportGeneratorAgent e simula un'analisi con dati di esempio.
class TestReportGeneratorAgent(unittest.TestCase):
    def test_generate_report(self):
        agent = ReportGeneratorAgent()
        analysis_data = {
            'issues': [
                {
                    'severity': 'Critical',
                    'message': 'Null pointer dereference',
                    'file': 'main.java',
                    'line': 45,
                    'description': 'This line of code may lead to a null pointer dereference.'
                },
                {
                    'severity': 'Major',
                    'message': 'Unused import statement',
                    'file': 'main.java',
                    'line': 10,
                    'description': 'This import statement is not used in the code.'
                }
            ]
        }

        ##Formato del report: 
        # Verifica che i problemi riscontrati dall'analisi siano correttamente inclusi nel report finale formattato.
        formatted_report = agent.tools[0].format_report(analysis_data)
        self.assertIn('Critical: Null pointer dereference', formatted_report)
        self.assertIn('Major: Unused import statement', formatted_report)

if __name__ == '__main__':
    unittest.main()
