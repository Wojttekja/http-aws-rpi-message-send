from asyncio import events
import json
import boto3

def lambda_handler(event, context):

    with open("/tmp/mode.txt", "w") as file:
        file.write(str(event))
    s3 = boto3.resource(u's3')
    bucket = s3.Bucket(u'swiatla')
    bucket.upload_file('/tmp/mode.txt', 'mode.txt')
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Polsak')
    }