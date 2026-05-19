import pandas as pd
from config import DATA_PATH


def load_data():
    """
    Load telecom dataset
    """

    try:
        df = pd.read_csv(DATA_PATH)

        print("Dataset loaded successfully.")

        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")

        return None


def clean_data(df):
    """
    Clean telecom dataset
    """

    # Remove unnamed columns
    unnamed_cols = [col for col in df.columns if "Unnamed" in col]

    if unnamed_cols:
        df.drop(columns=unnamed_cols, inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    df.fillna(0, inplace=True)

    print("Dataset cleaned successfully.")

    return df