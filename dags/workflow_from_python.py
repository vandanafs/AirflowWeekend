from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import porders
default_args = {
    'owners': 'Vandana',
    'start_date': datetime.today() - timedelta(days=1)
}
with DAG('PurchaseOrder_Data_Workflow', start_date=datetime(2022, 4, 1),
         schedule_interval='@once',
         catchup=False,
         default_args=default_args) as dag:
    task = PythonOperator(
        task_id='po_script',
        python_callable=porders,
        dag=dag
    )