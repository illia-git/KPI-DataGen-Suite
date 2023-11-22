import random

def generate_numeric_kpi(lower_bound, upper_bound, num_records, decimal_places=0):
    """Generates a list of random numeric KPI data."""
    return [round(random.uniform(lower_bound, upper_bound), decimal_places) for _ in range(num_records)]
