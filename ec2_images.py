#!/usr/bin/python

import boto3

ec2=boto3.resource('ec2')

response=ec2.images.all()

for image in response:
     print(image.id)
