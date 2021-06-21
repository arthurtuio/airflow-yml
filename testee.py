#from airflow import DAG
from datetime import timedelta, datetime


#from lib.operators.bigquery_to_hubspot import BigQueryToHubspot
#from lib.config.owner import Owner


default_args = {
    "owner": "Owner.MARKETING.name",
    "depends_on_past": False,
    "start_date": '2021-01-05',
    "email": "[Owner.MARKETING.value]",
    "email_on_failure": True,
    "email_on_retry": 3,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

