# from boto3 import resource
# from boto3.dynamodb.conditions import  Attr, Key
# from datetime import datetime

# db = resource('dynamodb')

# table = db.Table("demo-dynamo-python")
from app.config import settings

print(settings)

