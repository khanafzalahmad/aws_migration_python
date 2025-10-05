def transform_data(df, config):    
    """
    Applies transformations based on config:
    - Drops specified columns
    - Filters rows based on column and value
    """

    drop_cols = config.get("drop_columns", [])
    
    for col in drop_cols:
        if col in df.columns:
            df = df.drop(columns=[col])
    
    filter_config = config.get("filter",{})
    col = filter_config.get("column")
    val = filter_config.get("value")
    
    if col and val:
        df = df[df[col] == val]

    if 'unnecessary_column' in df.columns:
        df = df.drop(columns=['unnecessary_column'])

    df = df[df['status'] == 'active']
    return df