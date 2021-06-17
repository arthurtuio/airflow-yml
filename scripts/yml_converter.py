import os
import yaml
from jinja2 import Environment, FileSystemLoader


file_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(file_dir))

template = env.get_template('dag.template')

# I don't know what the configuration format but as long as you can convert to a dictionary, it can work.
values = {}
yaml_file = open("/home/arthur/clone_airflow_yml/airflow-yml/contexts/marketing_example/example_dag.yml")
values = yaml.load(yaml_file, Loader=yaml.FullLoader)

filename = os.path.join(file_dir, 'dag.py')

with open(filename, 'w') as fh:
    fh.write(template.render(
        dag_id="my_dag",
        num_task=1,
        **values
    ))
