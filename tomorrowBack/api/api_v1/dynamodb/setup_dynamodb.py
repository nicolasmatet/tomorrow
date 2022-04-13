import importlib
from boto_default import get_default_client, get_default_ressource
from execute_fixtures import execute_fixtures

models = importlib.import_module('tomorrowBack.api.api_v1.models')


def create_schema(client=None, ressouce=None):
    if not client:
        client = get_default_client()
    if not ressouce:
        ressouce = get_default_ressource()
    tables = []
    for modelName in models.__all__:
        modelClass = getattr(models, modelName)
        delete_table(modelName, client)
        tables.append(create_table(modelName, modelClass, ressouce))
    return tables


def delete_table(table_name, dynamodb=None):
    if not dynamodb:
        dynamodb = get_default_client()
    try:
        dynamodb.delete_table(TableName=table_name)
    except Exception as e:
        print(e)


def create_table(table_name, model, dynamodb=None):
    if not dynamodb:
        dynamodb = get_default_ressource()

    fields = [getattr(model, field) for field in model.__dict__ if not field.startswith('__') and not field == 'Meta']
    key_schema = [
        {
            'AttributeName': field.attributeName,
            'KeyType': field.keyType
        } for field in fields if field.keyType
    ]
    attribute_definitions = [
        {
            'AttributeName': field.attributeName,
            'AttributeType': field.attributeType
        } for field in fields if field.keyType
    ]

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput={
            'ReadCapacityUnits': model.Meta.readCapacityUnits,
            'WriteCapacityUnits': model.Meta.writeCapacityUnits
        }
    )
    return table


if __name__ == '__main__':
    tables = create_schema()
    execute_fixtures()
    print("Table status:", tables[0].table_status)
