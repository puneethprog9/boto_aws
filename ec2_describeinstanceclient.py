import boto3

ec2=boto3.client('ec2')

response=ec2.describe_instances()
for reservation in response["Reservations"]:
     for instance in reservation["Instances"]:     
             print(instance["Tags"][0]["Value"])
             print(instance["InstanceId"])
             print('---------------')

