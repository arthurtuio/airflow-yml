from datetime import timedelta, datetime

from airflow import DAG

from lib.config.owner import Owner


default_args = {
    "owner": Owner.MARKETING.name,
    "depends_on_past": False,
    "start_date": '2021-01-05',
    "email": [Owner.MARKETING.value],
    "email_on_failure": True,
    "email_on_retry": 3,
    "retries": 3,
    "retry_delay": 0:05:00,
}

dag = DAG(
    dag_id='example_send_data_from_bq_to_hubspot',
    catchup=False,
    default_args=default_args,
    max_active_runs=1,
    schedule_interval='@daily',
)

dag.doc_md = __doc__



"Melhor ter outro template a depender do tipo da task"


