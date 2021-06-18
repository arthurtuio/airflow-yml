"""
Código inutilizado
"""

def task_strategy_dict():
    """
    Lista de Operators que possuímos hoje
    :return:
    """
    return {
        "bigquery_hubspot": "BigQueryToHubspot",
    }


class MapTaskStrategy:
    def __init__(self, yml_dag_as_dict):
        self.yml_dag_as_dict = yml_dag_as_dict

    def execute(self):
        task_strategy = self._get_task_strategy()
        return self._build_task_object(task_strategy)

    def _get_task_strategy(self):
        if not (self.yml_dag_as_dict["source"] or self.yml_dag_as_dict["destination"]):
            raise Exception("Erro no yml! Os campos `source` e `destination` são obrigatórios!")

        strategy = "{}_{}".format(
            self.yml_dag_as_dict["source"],
            self.yml_dag_as_dict["destination"]
        )

        if strategy not in task_strategy_dict().keys():
            raise Exception("Task Strategy ainda não foi criada por DE")

        return strategy

    def _build_task_object(self, task_strategy):
        """
        Aqui eu construo o objeto task
        :param task_strategy:
        :return:
        """
        if task_strategy == "bigquery_hubspot":
            task_dict = {
                "operator": "BigQueryToHubspot",
                "bigquery_conn_id": self.yml_dag_as_dict.get(
                    "bigquery_conn_id", "gcp_airflow@contaazul-jarvis"
                ),
                "bigquery_sql": self.yml_dag_as_dict['source_sql'],
                "hubspot_conn_id": 1,
            }
