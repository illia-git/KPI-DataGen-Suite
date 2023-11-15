def save_to_csv(data_frame, file_path):
    """Saves the DataFrame to a CSV file.

    Args:
        data_frame (pd.DataFrame): The DataFrame to save.
        file_path (str): The path to the CSV file.
    """
    try:
        data_frame.to_csv(file_path, index=False)
        print(f"CSV file saved as {file_path}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")