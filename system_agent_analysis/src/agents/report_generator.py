import unittest
from agents.report_generator import ReportGeneratorAgent
from tools.formatting_tool import FormattingTool

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
        formatted_report = agent.tools[0].format_report(analysis_data)
        self.assertIn('Critical: Null pointer dereference', formatted_report)
        self.assertIn('Major: Unused import statement', formatted_report)

if __name__ == '__main__':
    unittest.main()
