"""
____________________________________________________
 Copyright 2018 Yicong Gong
 All rights reserved, for demostration purpose only.
____________________________________________________
This file provides elastic search capability.

"""
# 
from datetime import datetime
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from App.Utilities.config import aws_access_key_id, aws_secret_access_key
from App.Utilities.endpoints import REGION, ELASTIC_SEARCH_ENDPOINT, DEFAULT_USER_INDEX, USER_TYPE

awsauth = AWS4Auth(aws_access_key_id, aws_secret_access_key, 'us-west-1', 'es')
host = ELASTIC_SEARCH_ENDPOINT

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# index a document
def index_document(index, type, body, id = None):
    response = es.index(index=index, doc_type=type, id=id, body=doc)
    return response['result']

# index a user
def user_index(user_ID, userData):
    return index_document(DEFAULT_USER_INDEX, USER_TYPE, body = userData, id = user_ID)

# get a user by user_ID
def user_get(user_ID):
    response = es.get(index=DEFAULT_USER_INDEX, doc_type=USER_TYPE, id=user_ID)

def user_search(label):
    response = es.search(index=DEFAULT_USER_INDEX, body= {"query":
    {
        "bool" : {
            "should" : [
            {
                "prefix" : {
                "user_ID" : label
                }
            },
            {
                "match_phrase_prefix" : {
                "username" : label
                }
            },
            {
                "match_phrase_prefix" : {
                "fullName" : label
                }
            },
                        {
                "match_phrase_prefix" : {
                "firstName" : label
                }
            },
                        {
                "match_phrase_prefix" : {
                "email" : label
                }
            }
            ]
        }
        }})
    if response['hits']['total']:
        entryListFinal = []
        entryList = response['hits']['hits']
        for entry in entryList:
            entryListFinal.append(entry['_source'])
        return entryListFinal
    else:
        return False

if __name__ == '__main__':
    user_ID = 't12342'

    doc = {
        'email': 'test2@gmail.com',
        'lastName': 'Kim',
        'firstName': 'Kate2',
        'fullName': 'Kate2 Kim',
        'user_ID': 't12342',
        'username': 'theBestK2'
    }

    user_index(user_ID, userData = doc)

    print(user_search('Kate'))
