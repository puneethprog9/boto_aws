import boto3

client=boto3.client('s3')

client.delete_objects(Bucket='puneethboto3',Delete={'Objects':[{'Key':'chef_client.txt'}]})
