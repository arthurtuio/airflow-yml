## Automating Airflow DAGs using YAML

### Arquitetura do Repo:
- Pastas por contexto de negócio (ex: Marketing, Analytics, HR, etc), dentro da pasta `contexts/`;
  - Dentro de cada pasta, temos os YAMLs com as regras da criação da DAG, sendo 1 YAML = 1 DAG
- Pasta com os scripts de criação de DAGs, tanto de validação quanto criação de DAGs;
- Pasta de templates, uma vez que possuímos diversos operators, gerando a necessidade de diversos templates

### Como o código funciona
- A pessoa adiciona/atualiza o arquivo YAML com todas as informações necessárias para criar a DAG (
  para isso veja o `README` presente na pasta `contexts/`
  )
- O YAML é validado e criado usando a lib Python `cerberus`
- O arquivo Python é criado e enviado para a branch master, ou para o local de produção delas, por ex a pasta `dags/`

### Sobre as pastas:
- `contexts/`: Pasta onde ficam armazenados os YAMLs por contexto da empresa.  
Dentro dessa pasta há um README explicando os padrões de criação dos YAMLs

- `scripts/` : Scripts tanto para transformar YAML em DAG, quanto para validar se o YAML está correto
    - `yml_validator.py`: Validador de scripts YAMLs. Idealmente faz parte do CI, rodando sempre que um PR é aberto
    - `yml_converter.py`: Responsável por criar DAGs a partir do YAML
    - `send_dag_to_prod.py`: Responsável por enviar as DAGs para o local de produção delas, seja a pasta `dags/`,
nesse ou em outro repo.
    
- `dags/`: Pasta padrão do airflow, pode ficar nesse repositório ou em outro, ou até em outra branch. 

References:
  - https://medium.com/tech-grupozap/airflow-com-dags-em-yaml-dags-e-kubernetes-operator-d049865bb453
  - https://towardsdatascience.com/data-engineers-shouldnt-write-airflow-dags-part-2-8dee642493fb
  - https://stackoverflow.com/questions/66323798/reading-a-yaml-configuration-file-and-creating-a-dag-generator-in-airflow-2-0
