import boto3

s3=boto3.resource('s3')

obj=s3.Object('puneethboto3','chef_client.txt')

print(obj.content_type)
print(obj.last_modified)
