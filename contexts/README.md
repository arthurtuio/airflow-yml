# YAMLs creation

## Campos obrigatorios
Para entender como preencher cada campo, confira esta doc do confluence:
https://contaazul.atlassian.net/wiki/spaces/TTI/pages/edit-v2/2030568198

### Campos presentes em todas as DAGs, com exemplos
- **dag_name**: 
- **owner**: Owner.MARKETING.name
- **start_date**: 2019-01-05
- **schedule**: "@daily"

### Campos presentes na task
Na hora de criação da Task, é preciso que sejam preenchidos os seguintes campos
obrigatórios:
- tasks:
    - **name**: "send_data_from_bq_to_hubspot"
    - **source**: "bigquery"
    - **destination**: "hubspot"
    
Além destes, há campos que precisam ser preenchidos, a depender
do valor usado em **source** e **destination**.

Para ver a lista completa de possibilidades, acesse a documentação: <<link>>

Como exemplo, temos:
- tasks:
    - **name**: "send_data_from_bq_to_hubspot"
    - **source**: "bigquery"
    - **destination**: "hubspot"
    - **source_sql**: 
        ```` 
        """
        select
            email_contato as email,
            column1 as field_1,
            column2 as field_2
        from `project_example.schema_example.table_example`
        """ 
        ````
    - **destination_sql**: False (se houver SQL, botar o SQL)

### Campos opcionais
- **retries**: Default `3`, se quiser preencher fazer conforme o exemplo: "0"
- **retry_delay**: Default `timedelta(minutes=5)`, 
  se quiser preencher fazer conforme o exemplo: "timedelta(minutes=10)"
- **depends_on_past**: Default `False`, se quiser preencher fazer conforme o exemplo: True
- **email**: É preenchido automaticamente conforme o valor adicionado no campo **owner**
Se quiser adicionar um, basta adicionar conforme o exemplo: "youremail@contaazul.com"
- **email_on_failure**: Default `True`, se quiser preencher fazer conforme o exemplo: False
- **email_on_retry**: Default `False`, se quiser preencher fazer conforme o exemplo: True
- **catchup**: Default `False`, se quiser preencher fazer conforme o exemplo: True
- **max_active_runs**: Default `1`, se quiser preencher fazer conforme o exemplo: "2"


## Como criar um arquivo .yml
- Apenas salve o seu arquivo com a extensão `.yml`

