import credential
import boto3
import requests

object_name = "csv_data0.csv"

s3_client = boto3.client(
    's3',
    aws_access_key_id = credential.AccessKey,
    aws_secret_access_key = credential.SecretAccessKey
)

# generate the presigned URL
response = s3_client.generate_presigned_post(
    Bucket = "data-from-url-sophies",
    Key = object_name,
    ExpiresIn = 300
)

print(response)