import os
import yaml

from datetime import timedelta
from jinja2 import Environment, FileSystemLoader

from operator_mapping import operator_mapping
# from get_task_strategy import MapTaskStrategy


class ConvertYamlInDag:
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    DAGS_DIR = "/home/arthur/clone_airflow_yml/airflow-yml/dags"
    TEMPLATES_DIR = "/home/arthur/clone_airflow_yml/airflow-yml/templates"
    yaml_file = open("/home/arthur/clone_airflow_yml/airflow-yml/contexts/marketing_example/example_send_data_from_bq_to_hubspot.yml")
    YML_DAG_AS_DICT = yaml.load(yaml_file, Loader=yaml.FullLoader)

    def execute(self):
        enriched_dag = self._enrich_yml_dag_with_default_values(
            self.enrich_yml_dag_with_operator_values(self.YML_DAG_AS_DICT)
        )

        self.renderize_template_into_dag(
            yml_dag=enriched_dag,
            filename=self._set_filename(self.YML_DAG_AS_DICT),
            template=self._get_template()
        )

    def _set_filename(self, yml_dag):
        dag_name = yml_dag["dag_name"]

        return os.path.join(
            self.DAGS_DIR,
            '{}.py'.format(dag_name)
        )

    def _get_template(self):
        env = Environment(loader=FileSystemLoader(self.TEMPLATES_DIR))
        # print(env)

        template = env.get_template('dag.template')
        return template

    @staticmethod
    def renderize_template_into_dag(yml_dag, filename, template):
        with open(filename, 'w') as fh:
            fh.write(template.render(
                **yml_dag
            ))

    @staticmethod
    def _enrich_yml_dag_with_default_values(yml_dag_as_dict):
        yml_dag_as_dict["retries"] = yml_dag_as_dict.get("retries", 3)
        yml_dag_as_dict["retry_delay"] = yml_dag_as_dict.get("retry_delay", timedelta(minutes=5))
        yml_dag_as_dict["depends_on_past"] = yml_dag_as_dict.get("depends_on_past", False)
        yml_dag_as_dict["email_on_failure"] = yml_dag_as_dict.get("email_on_failure", True)
        yml_dag_as_dict["email_on_retry"] = yml_dag_as_dict.get("retries", False)
        yml_dag_as_dict["catchup"] = yml_dag_as_dict.get("catchup", False)
        yml_dag_as_dict["max_active_runs"] = yml_dag_as_dict.get("max_active_runs", 1)

        return yml_dag_as_dict

    @staticmethod
    def enrich_yml_dag_with_operator_values(yml_dag_as_dict):
        if not yml_dag_as_dict["tasks"]["operator"]:
            raise Exception("Campo operator obrigatório no arquivo YAML!")

        if yml_dag_as_dict["tasks"]["operator"] in operator_mapping():
            yml_dag_as_dict["tasks"]["operator_class"] = operator_mapping()[yml_dag_as_dict["tasks"]["operator"]]

        else:
            raise Exception("Operator ainda não foi criado por DE")

        return yml_dag_as_dict


if __name__ == '__main__':
    ConvertYamlInDag().execute()
