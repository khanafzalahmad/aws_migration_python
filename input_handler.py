import boto3
import pandas as pd
import io

def read_csv_file_s3(s3_path, region ="us-east-1"):
    """
    Reads a CSV file from S3 and returns a pandas DataFrame.
    """
    s3 = boto3.client("s3", region_name=region)
    bucket, key = s3_path.replace("s3://","").split("/", 1)
    obj = s3.get_object(Bucket=bucket, Key=key)
    return pd.read_csv(io.BytesIO(obj['Body'].read()))

def write_csv_file_s3(df, s3_path, region="us-east-1"):
    """
    Writes a pandas DataFrame to a CSV file in S3.
    """
    s3 = boto3.client("s3", region_name=region)
    bucket, key = s3_path.replace("s3://","").split("/", 1)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())


"""
def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error while reading the file {e}")
        return None
"""