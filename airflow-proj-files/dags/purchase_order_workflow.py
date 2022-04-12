from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
#from airflow.operators.papermill_operator import PapermillOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.utils.dates import days_ago

default_args={
    'owner':'vandana',
    'depends_on_past':False,
    'start_date':days_ago(1),     #datetime(2022,02,09),
    'email':['vandana.f.09@gmail.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':3,
    'retry_delay':timedelta(minutes=5),
    'schedule_interval':None,
    'catchup':False

}

def jupiter_operator():
    PapermillOperator(
        task_id='purchase_orders_notebook',
        input_nb='/Users/vandana/data_labs/Jy_projects/AirflowWeekend/purchase_orders.ipynb',
        output_nb='/Users/vandana/data_labs/Jy_projects/AirflowWeekend/out-{{ execution_date }}.ipynb',
        parameters={'msgs': "Ran from Airflow at {{ execution_date }}!"}
    )

dag = DAG('purchase_order_data_workflow',
          default_args=default_args,
          description='Purchase Order Data',
          schedule_interval='@daily'
          )

t1 = DummyOperator(task_id='data_workflow_start_here',
                   retries=3,
                   dag=dag)


def call_data():
    print('Purchase Order Data')


t2 = PythonOperator(task_id='purchase_order_data_workflow',
                    python_callable=call_data,
                    dag=dag)

t3 = PythonOperator(

    task_id='Jupiter_notebook',
    python_callable=jupiter_operator,
    dag=dag
)


t1 >> t2 >> t3