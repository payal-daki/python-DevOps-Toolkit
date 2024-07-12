#create s3 bucket using boto3  then list acl and disply output in dictionary format

import boto3
import json

# Create an S3 client
client = boto3.client('s3')

# Create a bucket
bucket_name = 'devpay-demo-boto3-s3'
create_response = client.create_bucket(
    Bucket=bucket_name,
)

# Print raw create bucket response
print("Create bucket response:")
print(create_response)
print()

# Get bucket ACL
acl_response = client.get_bucket_acl(
    Bucket=bucket_name,
)

# Print bucket ACL response
print("Bucket ACL response:")
print(acl_response)
print()

# Print owner's DisplayName and ID from ACL response
owner_display_name = acl_response['Owner']['DisplayName']
owner_id = acl_response['Owner']['ID']
print(f"Owner's DisplayName: {owner_display_name}")
print(f"Owner's ID: {owner_id}")
print()

# Print formatted JSON responses
print("Create bucket response (formatted):")
print(json.dumps(create_response, indent=4))
print()

print("Bucket ACL response (formatted):")
print(json.dumps(acl_response, indent=4))
