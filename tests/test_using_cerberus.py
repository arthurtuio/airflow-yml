import yaml
from yml_validator import validate


def test_validation_using_pytest():
    yaml_file = open("/home/arthur/clone_airflow_yml/airflow-yml/contexts/marketing_example/example_send_data_from_bq_to_hubspot.yml")
    obj = yaml.load(yaml_file, Loader=yaml.FullLoader)

    assert validate(obj) == True
