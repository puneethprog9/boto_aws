import boto3

client=boto3.client('ec2')

response=client.start_instances(
           InstanceIds=['i-0179827fc9a078372'])
