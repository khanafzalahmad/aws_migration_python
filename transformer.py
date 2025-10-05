def transform_data(df):    
    """
    Applies transformations:
    1. Drops 'unnecessary_column'.
    2. Filters rows where status == 'active'.
    """
    if 'unnecessary_column' in df.columns:
        df = df.drop(columns=['unnecessary_column'])

    df = df[df['status'] == 'active']
    return df