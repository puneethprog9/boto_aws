#!/usr/bin/python
import boto3

ec2=boto3.resource('ec2')
volume=ec2.volumes.all()

for i in volume:
   print(i.id)
