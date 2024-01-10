import boto3
from boto3.resources.base import ServiceResource
from .config import settings

def initialize_db() -> ServiceResource:
    ddb = boto3.resource('dynamodb',
                         region_name=settings.DB_REGION_NAME,
                         aws_access_key_id=settings.DB_ACCESS_KEY_ID,
                         aws_secret_access_key=settings.DB_SECRET_ACCESS_KEY)

    return ddb