def summarize_dataset(data, num_head=5, num_tail=5, drop_columns=None, drop_duplicates=False):
    """
    Veri çerçevesini özetleyen bir fonksiyon.

    Parameters:
    data (DataFrame): Özetlemek istediğiniz veri çerçevesi.
    num_head (int): İlk kaç satırın gösterileceğini belirler.
    num_tail (int): Son kaç satırın gösterileceğini belirler.
    drop_columns (list): Silmek istediğiniz sütunların listesi.
    drop_duplicates (bool): Yinelemeleri (duplikasyonları) veri çerçevesinden kaldırmak için kullanılır.

    Returns:
    DataFrame: İşlenmiş veri çerçevesi.
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
        if drop_columns:
            data.drop_duplicates(subset=drop_columns, inplace=True)
        else:
            data.drop_duplicates(inplace=True)
    

