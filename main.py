import logging
import yaml
from transformer import transform_data
from input_handler import read_csv_file_s3, write_csv_file_s3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    #file_path = 'sample_data.csv'
    #output_path = 'transformed_data.csv'
    #load config
    with open("config.yaml","r") as f:
        config = yaml.safe_load(f)

    region = config["aws"]["region"]
    input_s3_path = config["aws"]["input_file"]
    output_s3_path = config["aws"]["output_file"]
    transformations = config["transformations"]
    
    """
    input_file = config["input_file"]
    output_file = config["output_file"]
    transformations = config["transformations"]
    """

    logging.info("Starting data processing pipeline")


    # Step 1: Read data
    #df = read_csv_file(input_file)
    df = read_csv_file_s3(input_s3_path, region=region)
    
    if df is None:
        logging.error("Failed to read input file")
        return
    
    logging.info("Original Data:")
    logging.info(f"original data: {df}")

   # Step 2: Transform data
    transformed_df = transform_data(df, transformations)

    logging.info("Transformed Data:")
    logging.info(f"transformed data: {transformed_df}")

    # Step 3: Save transformed data
    #transformed_df.to_csv(output_file, index=False)
    write_csv_file_s3(transformed_df, output_s3_path, region=region)

    logging.info(f"Transformed data saved to {output_s3_path}")

if __name__ == "__main__":
    main()