import os

SERVER_ENDPOINT = os.environ.get('SERVER_ENDPOINT')
if not SERVER_ENDPOINT:
    SERVER_ENDPOINT = 'https://www.towntory.com/' # default
# SERVER_ENDPOINT = 'http://0.0.0.0:8000/' 

LOGIN_URL = SERVER_ENDPOINT + 'app/'
endpoints = {
    'root': SERVER_ENDPOINT,
    'write_url': SERVER_ENDPOINT + 'app/write',
    'landing_url': SERVER_ENDPOINT + 'app',
    'about_url': SERVER_ENDPOINT + 'app/about',
    'contact_url': SERVER_ENDPOINT + 'app/contact',
    'city_url': SERVER_ENDPOINT + 'app/city',
    'uploadImg': SERVER_ENDPOINT + 'app/uploadImg',
    'login_url': SERVER_ENDPOINT + 'accounts/login',
    'signup_url': SERVER_ENDPOINT + 'accounts/signup',
    'discover_url':SERVER_ENDPOINT + 'app/discover',
    'story_url': SERVER_ENDPOINT + 'app/story',
}

# Setting Endpoints
REGION = 'us-west-1'

# Elastic Search Endpoints
ELASTIC_SEARCH_ENDPOINT = ''
DEFAULT_USER_INDEX = ''
USER_TYPE = ''

### Production Endpoints ###
# S3 Bucket Endpoints
BUCKET_NAME = 'towntory'
BUCKET_URL_PREFIX = 'https://towntory.s3.amazonaws.com/'
# RDS Endpoints
DB_HOST = 'towntory.ceeyveabzx1x.us-west-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'towntory'

### DEvelopment Endpoints ###
# # S3 Bucket Endpoints
# BUCKET_NAME = 'fairytaler'
# BUCKET_URL_PREFIX = 'https://fairytaler.s3.amazonaws.com/'
# # RDS Endpoints
# DB_HOST = 'towntory.cxnifljcd06r.us-west-1.rds.amazonaws.com'
# DB_PORT = '5432'
# DB_NAME = 'towntory'