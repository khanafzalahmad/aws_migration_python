import pandas as pd

def read_csv_file(file_path):
    """
    Reads a CSV file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error while reading the file {e}")
        return None