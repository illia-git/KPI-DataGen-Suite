import numpy as np
import pandas as pd  # Import pandas

def generate_random_dates(start_date, end_date, num_dates):
    """Generates an array of random dates within a given range.

    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        num_dates (int): Number of dates to generate.

    Returns:
        numpy.ndarray: Array of randomly generated dates.
    """
    delta = (end_date - start_date).days
    random_days = np.random.randint(0, delta, num_dates)
    return start_date + pd.to_timedelta(random_days, unit='d')
