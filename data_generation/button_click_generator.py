import random

def generate_button_clicks(button_name, car_models, num_records):
    """Generates button click data for car models."""
    return [f"{button_name.lower()}.{random.choice(car_models)}" for _ in range(num_records)]
