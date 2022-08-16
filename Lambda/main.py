import json
import boto3

def lambda_handler(event, context):
    nowe = str(event)[10:]
    nowe = nowe[:len(nowe)-2]
    with open("/tmp/mode.txt", "w") as file:
        file.write(str(nowe))
    s3 = boto3.resource(u's3')
    bucket = s3.Bucket(u'light-control-app')
    bucket.upload_file('/tmp/mode.txt', 'mode.txt')
    return {
        'statusCode': 200,
        'body': "udalo sie"
    }
