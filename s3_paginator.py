import boto3

s3=boto3.client('s3')
paginator=s3.get_paginator('list_objects')
for page in paginator.paginate(Bucket='puneethboto3'):
     for obj in page['Contents']:
         print(obj['Key'])
