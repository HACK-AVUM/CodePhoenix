# tests/test_quality_control_crew.py
import unittest
from src.crews.quality_control_crew import QualityControlCrew

class TestQualityControlCrew(unittest.TestCase):
    def test_crew_execution(self):
        crew = QualityControlCrew()
        result = crew.kickoff(inputs={'project_key': 'my_project', 'source_code': 'sample_code'})
        self.assertIn('Code Quality Report', result)

if __name__ == '__main__':
    unittest.main()
