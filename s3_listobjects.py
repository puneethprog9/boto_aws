import boto3
import json
client=boto3.client('s3')

json1=client.list_objects(Bucket='puneethboto3')
last=len(json1['Contents'])
for list in range(last):
    print(json1['Contents'][list]['Key'])
