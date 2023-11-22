import unittest
from data_generation.numeric_kpi_generator import generate_numeric_kpi

class TestNumericKpiGenerator(unittest.TestCase):

    def test_generate_numeric_kpi_length(self):
        result = generate_numeric_kpi(1, 10, 5)
        self.assertEqual(len(result), 5)

    def test_generate_numeric_kpi_range(self):
        result = generate_numeric_kpi(1, 10, 5)
        for value in result:
            self.assertTrue(1 <= value <= 10)

if __name__ == '__main__':
    unittest.main()
