import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres():

    # PostgreSQL connection

    
    engine = create_engine(
    "postgresql+psycopg2://postgres:123456@telecom_postgres:5432/telecom_db"
    )
    
    # Read cleaned CSV

    df = pd.read_csv(
        "output/reports/cleaned_telecom_data.csv"
    )

    # Convert columns to lowercase

    df.columns = df.columns.str.lower()

    # Insert into PostgreSQL

    df.to_sql(
        "telecom_towers",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data inserted successfully.")


if __name__ == "__main__":
    load_to_postgres()