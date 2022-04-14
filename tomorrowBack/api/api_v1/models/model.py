import boto3
from botocore.exceptions import ClientError
import os

from api.settings import Settings

settings = Settings()

class Model:

    @classmethod
    def read(cls, key, db=None):
        print("endpoint_url", os.getenv('endpoint_url'))
        if db is None:
            db = boto3.resource('dynamodb', endpoint_url= settings.endpoint_url)
        table = db.Table('Question')
        print(db.get_available_subresources())
        print(table)
        try:
            response = table.get_item(Key=key)
        except ClientError as e:
            print(e)
        else:
            return response['Item']

    @classmethod
    def write(cls, item, db=None):
        if db is None:
            db = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        table = db.Table(cls.__name__)
        table.put_item(Item=item)
