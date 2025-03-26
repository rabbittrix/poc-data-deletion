from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from app.data_deletion import soft_delete_customer, get_all_customers

def trigger_soft_deletion():
    customers = get_all_customers()
    for customer in customers:
        customer_id, _, _, _, _ = customer
        soft_delete_customer(customer_id)
            
with DAG(
    'data_deletion_pipeline',
    description='Pipeline for deleting customer data',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='trigger_soft_deletion',
        python_callable=trigger_soft_deletion
    )