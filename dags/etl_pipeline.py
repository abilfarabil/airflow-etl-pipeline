from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.trigger_rule import TriggerRule
import pandas as pd
import json
import os
from sqlalchemy import create_engine

# Konfigurasi DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='etl_pipeline',
    default_args=default_args,
    description='ETL Pipeline untuk extract, transform, load data',
    schedule_interval='@daily',  # Menjalankan setiap hari
    start_date=days_ago(1),  # Agar DAG bisa langsung di-trigger
    catchup=False,
    params={'source_type': 'csv'}  # Set parameter untuk Trigger DAG dengan config
) as dag:

    def pilih_source(**kwargs):
        # Mengambil parameter dari UI
        source_type = kwargs.get('params').get('source_type', 'csv')
        print(f"Selected source type: {source_type}")  # Print parameter untuk debugging
        
        if source_type == 'csv':
            return 'extract_csv'
        elif source_type == 'json':
            return 'extract_json'
        else:
            raise ValueError("source_type harus 'csv' atau 'json'")  # Menangani kasus kesalahan

    branch_task = BranchPythonOperator(
        task_id='choose_source',
        python_callable=pilih_source,
        provide_context=True,
        dag=dag
    )

    def extract_csv():
        df = pd.read_csv('/opt/airflow/data/source_data/sales_data.csv')  # Sesuaikan path
        df.to_csv('/opt/airflow/data/staging/sales_data_staging.csv', index=False)

    extract_csv_task = PythonOperator(
        task_id='extract_csv',
        python_callable=extract_csv,
        dag=dag
    )

    def extract_json():
        with open('/opt/airflow/data/source_data/customers_data.json', 'r') as f:
            data = json.load(f)
        df = pd.json_normalize(data)
        df.to_csv('/opt/airflow/data/staging/customers_data_staging.csv', index=False)

    extract_json_task = PythonOperator(
        task_id='extract_json',
        python_callable=extract_json,
        dag=dag
    )

    def load_to_sqlite():
        # Perbaikan pada path database
        engine = create_engine('sqlite:////opt/airflow/data/output.db')  # Perhatikan tambahan '/' untuk path absolut
        
        # Memastikan file staging ada sebelum memuat
        if os.path.exists('/opt/airflow/data/staging/sales_data_staging.csv'):
            sales_data = pd.read_csv('/opt/airflow/data/staging/sales_data_staging.csv')
            sales_data.to_sql('sales', con=engine, if_exists='replace', index=False)

        if os.path.exists('/opt/airflow/data/staging/customers_data_staging.csv'):
            customers_data = pd.read_csv('/opt/airflow/data/staging/customers_data_staging.csv')
            customers_data.to_sql('customers', con=engine, if_exists='replace', index=False)

    load_to_sqlite_task = PythonOperator(
        task_id='load_to_sqlite',
        python_callable=load_to_sqlite,
        dag=dag,
        trigger_rule=TriggerRule.ONE_SUCCESS  # Menjalankan task ini jika salah satu task extract sukses
    )

    start_task = DummyOperator(task_id='start', dag=dag)
    end_task = DummyOperator(task_id='end', dag=dag)

    # Mengatur Alur Task (Dependencies)
    start_task >> branch_task
    branch_task >> [extract_csv_task, extract_json_task]
    extract_csv_task >> load_to_sqlite_task
    extract_json_task >> load_to_sqlite_task
    load_to_sqlite_task >> end_task
