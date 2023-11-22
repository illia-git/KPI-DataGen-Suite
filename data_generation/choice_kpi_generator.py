import random

def generate_random_choice_kpi(choices, num_records):
    """Generates a list of random choice KPI data."""
    return [random.choice(choices) for _ in range(num_records)]
