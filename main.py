from data_generation.date_generator import generate_random_dates
from data_generation.kpi_generator import generate_kpi_data
from utils.file_operations import save_to_csv
from datetime import datetime
import pandas as pd

def main():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 30)
    num_records = 200

    dates = generate_random_dates(start_date, end_date, num_records)
    kpi_data = generate_kpi_data(num_records)
    kpi_data["Date"] = dates.strftime("%Y-%m-%d")

    data_frame = pd.DataFrame(kpi_data)
    csv_file_path = 'sample_dashboard_data.csv'
    save_to_csv(data_frame, csv_file_path)

if __name__ == "__main__":
    main()
