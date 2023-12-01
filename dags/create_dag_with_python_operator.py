from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def get_name(ti):
    ti.xcom_push(key='first_name', value='Sophia')
    ti.xcom_push(key='last_name', value='Loren')


def get_age(ti):
    ti.xcom_push(key='age', value=44)


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f'HELLO WORLD! My name is {first_name} {last_name} and I am {age} years old.')


default_args = {
    'owner': 'amatacz',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='dag_ith_python_operator_v06',
    description='Our first DAG using Python operator',
    start_date=datetime(2023, 11, 28),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=greet,
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
