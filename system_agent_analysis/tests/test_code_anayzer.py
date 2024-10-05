## test_code_analyzer.py
#Testa l'agente di analisi del codice.

##Da aggiungere tutte le varie librerie necessarie per il testing (jUnit, ecc...)

import unittest
from src.agents.code_analyzer import CodeAnalyzerAgent

class TestCodeAnalyzerAgent(unittest.TestCase):
    def test_code_analysis(self):
        agent = CodeAnalyzerAgent()
        result = agent.tools[0].analyze_code('my_project', 'sample_code')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
