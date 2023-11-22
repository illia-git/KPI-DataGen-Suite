import random
from data_generation.numeric_kpi_generator import generate_numeric_kpi
from data_generation.choice_kpi_generator import generate_random_choice_kpi
from data_generation.journey_step_generator import generate_journey_steps
from data_generation.button_click_generator import generate_button_clicks
from data_generation.journey_config import CAR_MODELS, JOURNEYS, STEPS

def generate_kpi_data(num_records):
    """Generates random KPI data."""

    if num_records < 1:
        raise ValueError("Number of records must be positive.")

    return {
        "Total Visits": generate_numeric_kpi(800, 1500, num_records),
        "Unique Visitors": generate_numeric_kpi(700, 1200, num_records),
        "Avg Session Duration": generate_numeric_kpi(3, 10, num_records, 2),
        "Bounce Rate": generate_numeric_kpi(20, 70, num_records, 2),
        "Journeys Per Session": generate_numeric_kpi(1, 5, num_records),
        "Avg Time on Journey": generate_numeric_kpi(1, 5, num_records, 2),
        "Most Visited Journey": generate_random_choice_kpi(JOURNEYS, num_records),
        "Journey Steps": generate_journey_steps(JOURNEYS, STEPS, num_records),
        "Time on Step": generate_numeric_kpi(1, 5, num_records, 2),
        "TDA Clicks": generate_button_clicks("TDA", CAR_MODELS, num_records),
        "RFO Clicks": generate_button_clicks("RFO", CAR_MODELS, num_records),
        "Conversion Rate": generate_numeric_kpi(1, 10, num_records, 2),
        "Lead Conversion Rate": generate_numeric_kpi(0.5, 5, num_records, 2),
        "Document Downloads": generate_numeric_kpi(50, 200, num_records),
        "Purchases": generate_numeric_kpi(5, 30, num_records),
        "Feedback Score": generate_numeric_kpi(3, 5, num_records, 1),
        "Search Query Frequency": generate_random_choice_kpi(["new car models", "car pricing", "dealership locations"], num_records),
        "Search Result CTR": generate_numeric_kpi(20, 50, num_records, 2),
        "Social Shares": generate_numeric_kpi(40, 100, num_records),
        "Page Load Time": generate_numeric_kpi(1, 4, num_records, 2),
        "Error Rates": generate_numeric_kpi(0.01, 0.1, num_records, 2),
        "User Demographics": generate_random_choice_kpi(["25-34, Male", "35-44, Female", "18-24, Female"], num_records),
        "Behavioral Segment": generate_random_choice_kpi(["Returning Visitor", "New Visitor", "Frequent Buyer"], num_records)
    }