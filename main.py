from input_handler import read_csv_file
from transformer import transform_data

def main():
    # Step 1: Read data
    df = read_csv_file('sample_data.csv')
    if df is None:
        return
    
    print("Original Data:")
    print(df)

   # Step 2: Transform data
    transformed_df = transform_data(df)

    print("\nTransformed Data:")
    print(transformed_df)

if __name__ == "__main__":
    main()