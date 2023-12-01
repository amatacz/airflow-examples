from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'amatacz',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_cron_expression_v04',
    default_args=default_args,
    start_date=datetime(2023, 11, 10),
    schedule_interval='0 3 * * Tue-Fri'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo DAG with cron expression!'
    )

    task1
