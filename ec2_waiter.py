import boto3

ec2=boto3.client('ec2')

waiter = ec2.get_waiter('instance_running')

waiter.wait(InstanceIds=['i-0179827fc9a078372'])

print('Instance is ready!')
