import unittest
from data_generation.date_generator import generate_random_dates
from datetime import datetime

class TestDateGenerator(unittest.TestCase):
    def test_generate_random_dates(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 30)
        num_dates = 10
        dates = generate_random_dates(start_date, end_date, num_dates)
        self.assertEqual(len(dates), num_dates)
        # Additional assertions can be added for date range checks

if __name__ == '__main__':
    unittest.main()
