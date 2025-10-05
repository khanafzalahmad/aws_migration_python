import pandas as pd
from input_handler import read_csv_file
from transformer import transform_data

def test_read_csv_file():
    df = read_csv_file('sample_data.csv')
    assert df is not None
    assert len(df) == 5
    assert 'unnecessary_column' in df.columns

def test_tranform_data():
    df = pd.read_csv('sample_data.csv')
    transformed_df = transform_data(df)
    assert 'unnecessary_column' not in transformed_df.columns
    assert all(transformed_df["status"] == "active")
    assert len(transformed_df) == 3