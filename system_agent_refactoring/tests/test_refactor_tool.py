# tests/test_refactor_tool.py
import unittest
from src.tools.refactor_tool import RefactorTool

class TestRefactorTool(unittest.TestCase):
    def test_suggest_refactor(self):
        tool = RefactorTool()
        code_data = {'functions': 15, 'duplicate_code': True}
        suggestions = tool.suggest_refactor(code_data)
        self.assertEqual(len(suggestions), 2)

    def test_apply_refactor(self):
        tool = RefactorTool()
        code_data = {'functions': 15, 'duplicate_code': True}
        refactored_code = tool.apply_refactor(code_data)
        self.assertIsNotNone(refactored_code)

if __name__ == '__main__':
    unittest.main()
