import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection

USERNAME = "postgres"
PASSWORD = "123456"
HOST = "localhost"
PORT = "5432"
DATABASE = "telecom_db"

# Create engine

engine = create_engine(
    f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# SQL query

query = """
SELECT network,
       COUNT(*) AS towers_count,
       AVG(range) AS avg_range

FROM telecom_towers

GROUP BY network

ORDER BY towers_count DESC;
"""

# Read SQL query into pandas dataframe

df = pd.read_sql(query, engine)

# Show result

print(df)