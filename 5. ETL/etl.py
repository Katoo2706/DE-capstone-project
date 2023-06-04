
# airflow
import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator

# DAG args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email_on_failure': True,
    'email_on_retry': True,
    'email': ['katoo2706@gmail.com'],
    'retries': 0
}

# create the DAG
dag = DAG(
    dag_id="process_web_log",
    catchup=False,
    default_args=default_args,
    description='ETL pipeline for DE capstone project',
    schedule_interval="0 0 * * *"
)

# task definition
task_extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d" " -f1 ./capstone/accesslog.txt > ./capstone/extracted_data.txt',
    dag=dag
)

task_transform_Data = BashOperator(
    task_id='transform_data',
    bash_command='cat ./capstone/extracted_data.txt | grep "198.46.149.143" > ./capstone/transformed_data.txt',
    dag=dag
)

task_load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -czvf ./capstone/weblog.tar ./capstone/transformed_data.txt',
    dag=dag
)