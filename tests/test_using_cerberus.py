from config_test import validate_all_yaml_contexts


def test_validation_using_pytest():
    print(f"validate_all_yaml_contexts(): {validate_all_yaml_contexts()}")
    print(f"resultado do all: {all(validate_all_yaml_contexts())}")
    print(type(all(validate_all_yaml_contexts())))
    assert all(validate_all_yaml_contexts()) is True


if __name__ == '__main__':
    print(validate_all_yaml_contexts())
    test_validation_using_pytest()
