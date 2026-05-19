from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys

# Add project path
sys.path.append('/opt/airflow')

from src.database import load_to_postgres

default_args = {
    'owner': 'Mohamed',
    'start_date': datetime(2026, 5, 18),
}

with DAG(
    dag_id='telecom_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    load_data_task = PythonOperator(
        task_id='load_telecom_data',
        python_callable=load_to_postgres
    )

    load_data_task