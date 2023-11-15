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
        "Total Visits": np.random.randint(800, 1500, num_records),
        "Unique Visitors": np.random.randint(700, 1200, num_records),
        "Avg Session Duration": np.round(np.random.uniform(3, 10, num_records), 2),
        "Bounce Rate": np.round(np.random.uniform(20, 70, num_records), 2),
        "Journeys Per Session": np.random.randint(1, 5, num_records),
        "Avg Time on Journey": np.round(np.random.uniform(1, 5, num_records), 2),
        "Most Visited Journey": np.random.choice(
            ["Car Configurator", "Dealer Search", "Inventory Check"], num_records
        ),
        "Conversion Rate": np.round(np.random.uniform(1, 10, num_records), 2),
        "Lead Conversion Rate": np.round(np.random.uniform(0.5, 5, num_records), 2),
        "Document Downloads": np.random.randint(50, 200, num_records),
        "Purchases": np.random.randint(5, 30, num_records),
        "Feedback Score": np.round(np.random.uniform(3, 5, num_records), 1),
        "Search Query Frequency": np.random.choice(
            ["new car models", "car pricing", "dealership locations"], num_records
        ),
        "Search Result CTR": np.round(np.random.uniform(20, 50, num_records), 2),
        "Social Shares": np.random.randint(40, 100, num_records),
        "Page Load Time": np.round(np.random.uniform(1, 4, num_records), 2),
        "Error Rates": np.round(np.random.uniform(0.01, 0.1, num_records), 2),
        "User Demographics": np.random.choice(
            ["25-34, Male", "35-44, Female", "18-24, Female"], num_records
        ),
        "Behavioral Segment": np.random.choice(
            ["Returning Visitor", "New Visitor", "Frequent Buyer"], num_records
        )
    }
