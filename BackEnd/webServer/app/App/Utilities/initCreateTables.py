"""
____________________________________________________
 Copyright 2018 Yicong Gong
 All rights reserved, for demostration purpose only.
____________________________________________________
This file provides low-level DynamoDB interfaces.

"""
# Imports
import boto3
from boto3.dynamodb.conditions import Key, Attr
from credentials import aws_access_key_id, aws_secret_access_key

# table names
EMAIL_LOOKUP_TABLE = 'authSerive_Email_Lookup'
EXP_ID_LOOKUP_TABLE = 'authSerive_Exp_ID_Lookup'
USER_TABLE = 'authSerive_User_Table'

# Get the service resource.

dynamodb = boto3.resource('dynamodb', region_name='us-west-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,)

## Create table
def create_table(table_name, partitionKeyName, sortingKeyName = None):
    # Create the DynamoDB table.
    if sortingKeyName:
        table = dynamodb.create_table(
            TableName = table_name,
            KeySchema=[
                {
                    'AttributeName': partitionKeyName,
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': sortingKeyName,
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': partitionKeyName,
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': sortingKeyName,
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

    else:
        table = dynamodb.create_table(
            TableName = table_name,
            KeySchema=[
                {
                    'AttributeName': partitionKeyName,
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': partitionKeyName,
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        

if __name__ == '__main__':
    create_table('STORY_TABLE', 'story_id')
    # create_table('COMMENT_TABLE', 'story_id')