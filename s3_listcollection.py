import boto3

s3=boto3.resource('s3')

for obj in s3.Bucket(name='puneethboto3').objects.all():
    print(obj.key)
