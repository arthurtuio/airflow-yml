from airflow import DAG
from datetime import timedelta, datetime


from lib.operators.bigquery_to_hubspot import BigQueryToHubspot
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




example_task_send_data_from_bq_to_hubspot = BigQueryToHubspot(
    task_id="example_task_send_data_from_bq_to_hubspot",
    bigquery_conn_id="gcp_airflow@contaazul-jarvis",
    bigquery_sql=" select email_contato as email, column1 as field_1, column2 as field_2 from `project_example.schema_example.table_example` ",
    hubspot_conn_id="http_hubspot_acc",
    throw_exception_on_invalid_email=False,
    depends_on_past=False,
    dag=dag,
)

