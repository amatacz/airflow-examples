from datetime import datetime, timedelta, timezone
import pytz

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'amatacz',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

tz = pytz.timezone("Europe/Warsaw")

with DAG(
    dag_id='our_first_dag_v5',
    description='This is our first dag that we write.',
    default_args=default_args,
    start_date=datetime(2023, 11, 29, 18, 56, tzinfo=tz),
    # schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is the first task!'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hey, I am the second task and I will be executed after task1'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hey, I am the third task and I will be executed after task1, parallel to task2'
    )

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]