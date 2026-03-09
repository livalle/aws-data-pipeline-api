from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from ingestion.api_to_s3 import ingest

with DAG(
    dag_id="api_data_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="ingest_api",
        python_callable=ingest
    )
