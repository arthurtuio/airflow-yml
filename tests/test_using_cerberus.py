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


def test_validation_using_pytest():
    for yaml_file in get_all_contexts():
        obj = yaml.load(open(yaml_file), Loader=yaml.FullLoader)
        print(obj)
        print(type(obj))

        assert validate(obj) == True


if __name__ == '__main__':
    get_all_contexts()
    test_validation_using_pytest()