import unittest
from data_generation.button_click_generator import generate_button_clicks

class TestButtonClickGenerator(unittest.TestCase):

    def test_generate_button_clicks(self):
        car_models = ["model1", "model2"]
        result_tda = generate_button_clicks("TDA", car_models, 5)
        result_rfo = generate_button_clicks("RFO", car_models, 5)
        self.assertEqual(len(result_tda), 5)
        self.assertEqual(len(result_rfo), 5)
        for click in result_tda:
            self.assertTrue(any(model in click for model in car_models))
        for click in result_rfo:
            self.assertTrue(any(model in click for model in car_models))

if __name__ == '__main__':
    unittest.main()
