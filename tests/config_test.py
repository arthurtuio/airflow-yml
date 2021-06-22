import os
import yaml

from yml_validator import validate


HOME_FOLDER = os.getcwd() + '/'
CONTEXTS_DIR = HOME_FOLDER + 'contexts/'


def get_all_contexts():
    """
    parece que o pytest nao consegue usar o os pra ler arquivos
    :return:
    """
    # print(f'home_folder: {HOME_FOLDER}')
    # print(f'contexts_dir: {CONTEXTS_DIR}')

    files_list = []

    for filename in os.listdir(CONTEXTS_DIR):
        # print(f'filename: {filename}')
        # print(f'filename com a pasta: {CONTEXTS_DIR + filename}')
        if os.path.isdir(CONTEXTS_DIR + filename):
            dir = CONTEXTS_DIR + filename

            for file in os.listdir(dir):
                # print(f'file dentro do dir: {file}')
                # print(f"file dentro do dir com a pasta: {dir + '/' + file}")
                file_in_folder = dir + '/' + file
                files_list.append(file_in_folder)

    print(f'files_list: {files_list}')

    return files_list


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
