import os
import yaml

from yml_validator import validate


BASE_REPO_DIR = os.path.normpath(os.getcwd() + os.sep + os.pardir)
CONTEXTS_DIR = BASE_REPO_DIR + "/contexts"


def get_all_contexts():
    """
    parece que o pytest nao consegue usar o os pra ler arquivos
    :return:
    """
    files_list = []
    print(f'BASE_REPO_DIR: {BASE_REPO_DIR}')
    # print(f'os.walk(CONTEXTS_DIR): {os.walk(CONTEXTS_DIR)}')

    for subdir, dirs, files in os.walk(CONTEXTS_DIR):
        print(f'subdir, dirs, files: {(subdir, dirs, files)}')
        for file in files:
            print(f'file: {file}')
            print(os.path.join(subdir, file))
            if not file.endswith(".md"):
                files_list.append(os.path.join(subdir, file))

    # print(f"files_list: {files_list}")
    return files_list
    # return ["/home/arthur/clone_airflow_yml/airflow-yml/contexts/marketing_example/example_send_data_from_bq_to_hubspot.yml"]


def transform_contexts_in_yamls():
    return [
        yaml.load(open(yaml_file), Loader=yaml.FullLoader)
        for yaml_file in get_all_contexts()
    ]


def validate_all_yaml_contexts():
    get_all_contexts()
    return [validate(yaml_context) for yaml_context in transform_contexts_in_yamls()]


if __name__ == '__main__':
    # print(get_all_contexts())
    print(validate_all_yaml_contexts())
