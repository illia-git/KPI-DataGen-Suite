import random

def generate_journey_steps(journeys, steps, num_records):
    """Generates detailed steps for each journey."""
    journey_steps = []
    for _ in range(num_records):
        journey = random.choice(journeys)
        journey_steps.append(random.choice(steps[journey]))
    return journey_steps
