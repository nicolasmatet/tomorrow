import boto3
from api.settings import Settings

settings = Settings()

def get_default_client(): return boto3.client('dynamodb', endpoint_url=settings.endpoint_url)


def get_default_ressource(): return boto3.resource('dynamodb', endpoint_url=settings.endpoint_url)
