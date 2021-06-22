import yaml
from cerberus import Validator


def default_params_base():
    return {
        'dag_name': {'type': 'string'},
        'owner': {'type': 'string'},
        'start_date': {'type': 'string'},
        'schedule': {'type': 'string'},
    }


def task_params_base():
    return {
        'tasks': {
            'type': 'dict',
            'schema': {
                'name': {'type': 'string'},
                'operator': {'type': 'string'},
                # 'destination': {'type: string'},
                # 'source': {'type': 'string'},
                'source_sql': {'type': 'string'},
                # 'destination_sql': {'type': 'boolean'},
            }
        }
    }


def validate(obj_to_validate):
    validator_obj = Validator(
        {
            **default_params_base(),
            **task_params_base(),
        }
    )
    return validator_obj(obj_to_validate)  # vai retornar True ou False


if __name__ == '__main__':
    yaml_file = open("/home/arthur/clone_airflow_yml/airflow-yml/contexts/marketing_example/example_send_data_from_bq_to_hubspot.yml")
    obj = yaml.load(yaml_file, Loader=yaml.FullLoader)

    #print(obj)

    print(validate(obj))
