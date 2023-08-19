def summarize_dataset(data, num_head=5, num_tail=5):
    """
    Veri çerçevesini özetleyen bir fonksiyon.

    Parameters:
    data (DataFrame): Özetlemek istediğiniz veri çerçevesi.
    num_head (int): İlk kaç satırın gösterileceğini belirler.
    num_tail (int): Son kaç satırın gösterileceğini belirler.

    Returns:
    None
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
    
    print(f"Missing Values:\n{data.isnull().sum()}")
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
    
    
    
