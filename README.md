## Automating Airflow DAGs using YAML

### Arquitetura do Repo:
- Pastas por contexto de negócio (ex: Marketing, Analytics, HR, etc)
- Dentro de cada pasta, temos os YAMLs com as regras da criação da DAG, sendo 1 YAML = 1 DAG
- Outra pasta com os scripts de criação de DAGs, convertendo de YAML para Python.

### Sobre as pastas:
- `contexts/`: Pasta onde ficam armazenados os YAMLs por contexto da empresa.  
Dentro dessa pasta há um README explicando os padrões de criação dos YAMLs

- `scripts/` : Scripts tanto para transformar YAML em DAG, quanto para validar se o YAML está correto
    - `yml_validator.py`: Validador de scripts YAMLs. Idealmente faz parte do CI, rodando sempre que um PR é aberto
    - `yml_converter.py`: Responsável por criar DAGs a partir do YAML
    - `send_dag_to_prod.py`: Responsável por enviar as DAGs para o local de produção delas, seja a pasta `dags/`,
nesse ou em outro repo.
    
- `dags/`: Pasta padrão do airflow, pode ficar nesse repositório ou em outro. 

References:
    - https://medium.com/tech-grupozap/airflow-com-dags-em-yaml-dags-e-kubernetes-operator-d049865bb453

