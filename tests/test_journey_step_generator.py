import unittest
from data_generation.journey_step_generator import generate_journey_steps

class TestJourneyStepGenerator(unittest.TestCase):

    def test_generate_journey_steps(self):
        journeys = ["Journey1", "Journey2"]
        steps = {
            "Journey1": ["step1", "step2"],
            "Journey2": ["step3", "step4"]
        }
        result = generate_journey_steps(journeys, steps, 10)
        self.assertEqual(len(result), 10)
        for step in result:
            self.assertTrue(step in steps["Journey1"] or step in steps["Journey2"])

if __name__ == '__main__':
    unittest.main()
