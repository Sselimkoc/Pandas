def summarize_dataset(data, num_head=5, num_tail=5, drop_columns=None, drop_duplicates=False):
    """
    Summarizes a DataFrame.

    Parameters:
    data (DataFrame): The DataFrame to summarize.
    num_head (int): Specifies how many rows to display from the beginning.
    num_tail (int): Specifies how many rows to display from the end.
    drop_columns (list): List of columns to drop.
    drop_duplicates (bool): Used to remove duplicates from the DataFrame.

    Returns:
    DataFrame: The processed DataFrame.
    """
    print(f"First {num_head} rows:")
    print(data.head(num_head))
    print("\n")
    
    print(f"Last {num_tail} rows:")
    print(data.tail(num_tail))
    print("\n")
    
    print("Columns:")
    print(data.columns)
    print("\n")

    print("Data Information:")
    data.info()
    print("\n")
    
    missing_values = data.isnull().sum()
    missing_columns = missing_values[missing_values > 0]
    print(f"Missing Values:\n{missing_columns}")
    print("\n")
    
    print("Statistical Summary:")
    print(data.describe())
    print("\n")
    
    print("Data Shape:")
    print(data.shape)
    print("\n")
    
    num_duplicates = data.duplicated().sum()
    print(f"Number of duplicated rows: {num_duplicates}")
    print("\n")

    if drop_duplicates:
        initial_rows = data.shape[0]  
        if drop_columns:
            data.drop_duplicates(subset=drop_columns, inplace=True)
        else:
            data.drop_duplicates(inplace=True)
        dropped_rows = initial_rows - data.shape[0]  
        print(f"Number of dropped rows: {dropped_rows}")
    return data
