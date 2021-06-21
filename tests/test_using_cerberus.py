import os
import yaml

from yml_validator import validate


BASE_REPO_DIR = os.path.normpath(os.getcwd() + os.sep + os.pardir)
CONTEXTS_DIR = BASE_REPO_DIR + "/contexts"


def get_all_contexts():
    files_list = []

    for subdir, dirs, files in os.walk(CONTEXTS_DIR):
        for file in files:
            # print(os.path.join(subdir, file))
            if not file.endswith(".md"):
                files_list.append(os.path.join(subdir, file))

    # print(files_list)
    return files_list


def transform_contexts_in_yamls():
    return [
        yaml.load(open(yaml_file), Loader=yaml.FullLoader)
        for yaml_file in  get_all_contexts()
    ]


def validate_all_yaml_contexts():
    return [validate(yaml_context) for yaml_context in transform_contexts_in_yamls()]


def test_validation_using_pytest():
    assert any(validate_all_yaml_contexts()) == True


if __name__ == '__main__':
    get_all_contexts()
    # print(transform_contexts_in_yamls())
    # print(validate_all_yaml_contexts())
    test_validation_using_pytest()
