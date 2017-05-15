#!/usr/bin/python

import boto3

ec2=boto3.client('ec2')

response=ec2.describe_vpcs(VpcIds=['vpc-4c59ce25'])

print(response)
