from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'amatacz',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)

}


def get_sklearn():
    import sklearn
    print(f'scikit-lear with version: {sklearn.__version__}')


def get_matplotlib():
    import matplotlib
    print(f'matplotlib version: {matplotlib.__version__}')


with DAG(
    dag_id='dag_with_python_dependencies_v01',
    default_args=default_args,
    start_date=datetime(2023, 12, 4),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='sklear-version',
        python_callable=get_sklearn
    )
    task2 = PythonOperator(
        task_id='matplotlib-version',
        python_callable=get_matplotlib
    )

    task1 >> task2
