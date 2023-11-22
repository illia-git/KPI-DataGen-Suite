import unittest
from data_generation.choice_kpi_generator import generate_random_choice_kpi

class TestChoiceKpiGenerator(unittest.TestCase):

    def test_generate_random_choice_kpi(self):
        choices = ["A", "B", "C"]
        result = generate_random_choice_kpi(choices, 10)
        self.assertEqual(len(result), 10)
        for choice in result:
            self.assertIn(choice, choices)

if __name__ == '__main__':
    unittest.main()
