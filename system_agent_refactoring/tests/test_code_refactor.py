# tests/test_code_refactor.py
import unittest
from src.agents.code_refactor import CodeRefactorAgent

class TestCodeRefactorAgent(unittest.TestCase):
    def test_suggest_refactor(self):
        agent = CodeRefactorAgent()
        code_data = {'functions': 15, 'duplicate_code': True}
        suggestions = agent.suggest_refactor(code_data)
        self.assertIn('breaking down large functions', suggestions)
        self.assertIn('duplicates', suggestions)

if __name__ == '__main__':
    unittest.main()
