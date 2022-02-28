import boto3
import logging
import sys
# 'start_ec2instance'
# arn:aws:iam::108172868018:role/x_lambda

def lambda_build(LambdaFunctionName, RoleName):

    client = boto3.client(
        'lambda', 
        region_name='us-east-1',
        aws_access_key_id='AKIARSL427GZFQ2VV5X4',
        aws_secret_access_key='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'
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