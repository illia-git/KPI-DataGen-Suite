import unittest
from data_generation.kpi_generator import generate_kpi_data

class TestKpiGenerator(unittest.TestCase):

    def test_generate_kpi_data(self):
        num_records = 10
        kpi_data = generate_kpi_data(num_records)
        
        expected_keys = [
            "Total Visits", "Unique Visitors", "Avg Session Duration", 
            "Bounce Rate", "Journeys Per Session", "Avg Time on Journey", 
            "Most Visited Journey", "Journey Steps", "Time on Step",
            "TDA Clicks", "RFO Clicks", "Conversion Rate", 
            "Lead Conversion Rate", "Document Downloads", "Purchases", 
            "Feedback Score", "Search Query Frequency", "Search Result CTR", 
            "Social Shares", "Page Load Time", "Error Rates", 
            "User Demographics", "Behavioral Segment"
        ]

        self.assertIsInstance(kpi_data, dict)
        self.assertEqual(set(kpi_data.keys()), set(expected_keys))

        for key, value in kpi_data.items():
            with self.subTest(key=key):
                self.assertEqual(len(value), num_records)
                # Additional tests can be added for specific data types or value ranges

if __name__ == '__main__':
    unittest.main()
