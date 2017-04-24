import boto3
import json
ec2=boto3.resource('ec2')

#response=ec2.describe_instances()

#print(response["Reservations"]["Instances"])

response=ec2.instances.all()

for i in response:
      print(i.tags[0]['Value'])
      print(i.id)
      print(i.image.id)
      print(i.subnet.id)
      print(i.vpc.id)
      print('------------')
