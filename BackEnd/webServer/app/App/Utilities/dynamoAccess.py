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

# Get the service resource.
try: 
    # provide config.py for local testing
    # if config.py not present, use IAM role instead
    from credentials import aws_access_key_id, aws_secret_access_key
    dynamodb = boto3.resource('dynamodb', region_name='us-west-1',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,)
except:
    dynamodb = boto3.resource('dynamodb',region_name='us-west-1')

# add edge
def add(table_name, partitionKeyName, partitionKey, sortingKeyName = None, sortingKey = None, **kwargs): 
    
    table = dynamodb.Table(table_name)
    data = {partitionKeyName: partitionKey}
    if sortingKeyName and sortingKey:
        data[sortingKeyName] = sortingKey
    for key in kwargs:
        data[key] = kwargs[key]
    response = table.put_item(
        Item = data
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False

# delete edge
def delete(table_name, partitionKeyName, partitionKey, sortingKeyName = None, sortingKey = None):
    
    table = dynamodb.Table(table_name)
    if sortingKeyName and sortingKey:
        response = table.delete_item(
            Key={
                partitionKeyName: partitionKey,
                sortingKeyName: sortingKey,
            }
        )
    else:
        response = table.delete_item(
            Key={
                partitionKeyName: partitionKey
            }
        )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False

# query
def query(table_name, partitionKeyName, partitionKey):
    table = dynamodb.Table(table_name)
    # query
    response = table.query(
        KeyConditionExpression=Key(partitionKeyName).eq(partitionKey)
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return response['Items']
    else:
        return False

# get item
def get_item(table_name, partitionKeyName, partitionKey, sortingKeyName = None, sortingKey = None):
    table = dynamodb.Table(table_name)
    if sortingKeyName and sortingKey:
        response = table.get_item(
            Key={
                partitionKeyName: partitionKey,
                sortingKeyName: sortingKey,
            }
        )
    else:
        response = table.get_item(
            Key={
                partitionKeyName: partitionKey
            }
        )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return response['Item']
    else:
        return False

if __name__ == '__main__':
    pass
