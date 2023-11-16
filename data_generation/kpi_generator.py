import numpy as np
import random

def generate_kpi_data(num_records):
    """Generates random KPI data.

    Args:
        num_records (int): Number of records to generate.

    Returns:
        dict: Dictionary containing KPI data.
    """
    return {
        "Total Visits": [random.randint(800, 1500) for _ in range(num_records)],
        "Unique Visitors": [random.randint(700, 1200) for _ in range(num_records)],
        "Avg Session Duration": [round(random.uniform(3, 10), 2) for _ in range(num_records)],
        "Bounce Rate": [round(random.uniform(20, 70), 2) for _ in range(num_records)],
        "Journeys Per Session": [random.randint(1, 5) for _ in range(num_records)],
        "Avg Time on Journey": [round(random.uniform(1, 5), 2) for _ in range(num_records)],
        "Most Visited Journey": [random.choice(["Car Configurator", "Dealer Search", "Inventory Check"]) for _ in range(num_records)],
        "Conversion Rate": [round(random.uniform(1, 10), 2) for _ in range(num_records)],
        "Lead Conversion Rate": [round(random.uniform(0.5, 5), 2) for _ in range(num_records)],
        "Document Downloads": [random.randint(50, 200) for _ in range(num_records)],
        "Purchases": [random.randint(5, 30) for _ in range(num_records)],
        "Feedback Score": [round(random.uniform(3, 5), 1) for _ in range(num_records)],
        "Search Query Frequency": [random.choice(["new car models", "car pricing", "dealership locations"]) for _ in range(num_records)],
        "Search Result CTR": [round(random.uniform(20, 50), 2) for _ in range(num_records)],
        "Social Shares": [random.randint(40, 100) for _ in range(num_records)],
        "Page Load Time": [round(random.uniform(1, 4), 2) for _ in range(num_records)],
        "Error Rates": [round(random.uniform(0.01, 0.1), 2) for _ in range(num_records)],
        "User Demographics": [random.choice(["25-34, Male", "35-44, Female", "18-24, Female"]) for _ in range(num_records)],
        "Behavioral Segment": [random.choice(["Returning Visitor", "New Visitor", "Frequent Buyer"]) for _ in range(num_records)]
    }
