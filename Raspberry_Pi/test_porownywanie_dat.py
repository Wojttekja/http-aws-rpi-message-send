import boto3
import botostubs
import datetime

s3 = boto3.resource("s3")
response = s3.Object(bucket_name="light-control-app", key="mode.txt").__getattribute__("last_modified")

print(response)
print(type(response))