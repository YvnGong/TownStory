"""
____________________________________________________
 Copyright 2018 Yicong Gong
 All rights reserved, for demostration purpose only.
____________________________________________________
This file provides S3 access capability.

"""
import boto3
import uuid
from App.Utilities.endpoints import REGION, PROFILE_PIC_BUCKET, BUCKER_URL_PREFIX

try:
    from App.Utilities.config import aws_access_key_id, aws_secret_access_key
    s3 = boto3.client(
        's3',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
        region_name=REGION
    )

except:
    s3 = boto3.client('s3')

def generate_presigned_upload_url(bucket_name, key = None, timeout = 3600, method = 'PUT'):
    if not key:
        key = generate_image_name()
    try:
        uploadURL = s3.generate_presigned_url('put_object', 
            Params={'Bucket':bucket_name, 'Key':key, 'ACL':'public-read'}, 
            ExpiresIn=timeout, 
            HttpMethod=method)
        accessURL = BUCKER_URL_PREFIX + key
        return (uploadURL, accessURL)
    except:
        return False

def get_url(bucket_name, key, timeout = 3600, method = 'GET'):
    try:
        url = s3.generate_presigned_url('get_object', 
            Params={'Bucket':bucket_name, 'Key':key}, 
            ExpiresIn=timeout, 
            HttpMethod=method)
        return url
    except:
        return False

def upload_file(bucket_name, fileobj):
    try:
        key = generate_image_name()
        s3.upload_fileobj(fileobj, bucket_name, key, ExtraArgs={'ACL':'public-read'})
        return BUCKER_URL_PREFIX + key
    except:
        return False


def generate_image_name():
    name = str(uuid.uuid4())
    return name


if __name__ == '__main__':
    print(generate_presigned_upload_url(PROFILE_PIC_BUCKET))
    # print(get_url(PROFILE_PIC_BUCKET, 'test10.jpg'))
