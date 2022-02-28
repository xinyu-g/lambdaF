import boto3
import logging
import sys


def lambda_build(LambdaFunctionName, RoleName):

    client = boto3.client(
        'lambda', 
        region_name='us-east-1',
        aws_access_key_id='',
        aws_secret_access_key=''
    )

    create_lambda_function = client.create_function(
        FunctionName=LambdaFunctionName,
        Runtime='python3.7',
        Role=RoleName,
        Handler='{}.lambda_handler'.format('lambda_build'),
        Description='Get Request',
        Code={'S3Bucket': 'qchangebucket', 'S3Key': 'get_complements.zip'}
    )



LambdaFunctionName = sys.argv[1]
RoleName = sys.argv[2]

lambda_build(LambdaFunctionName, RoleName)