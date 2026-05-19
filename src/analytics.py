def dataset_overview(df):
    """
    Show dataset overview
    """

    print("\n===== Dataset Shape =====")
    print(df.shape)

    print("\n===== Dataset Columns =====")
    print(df.columns)

    print("\n===== Data Types =====")
    print(df.dtypes)

    print("\n===== Missing Values =====")
    print(df.isnull().sum())


def network_distribution(df):
    """
    Network distribution
    """

    return df["Network"].value_counts()


def radio_distribution(df):
    """
    Radio technology distribution
    """

    return df["radio"].value_counts()


def country_distribution(df):
    """
    Country distribution
    """

    return df["Country"].value_counts()


def range_statistics(df):
    """
    Telecom range statistics
    """

    return df["RANGE"].describe()


def average_coordinates(df):
    """
    Average coordinates
    """

    return {
        "Average Latitude": df["LAT"].mean(),
        "Average Longitude": df["LON"].mean()
    }