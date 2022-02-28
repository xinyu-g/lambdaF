# README

To create the lambda function, follow the steps below

## 1. Create AWS account

## 2. [Create an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)

## 3. [Create a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

## 4. Create a S3 bucket

## 5. Upload .zip file to the s3 bucket

## 6. Open a terminal and navigate to the directory that contains the *lambda_build.py* script

```python
python ./lambda_build.py '[FunctionName]' '[lambda_role_arn]'
```

## 7. Go to Lambda service on AWS

1. Navigate to the lambda function and find **Function code**
2. Change the **Handler** to **get_complements.get**

## 8. Add API Gateway

	1. Under **Functional overview**, choose **Add trigger** 
	1. choose the lambda function
	1. select **API Gateway**
	1. choose **Create an API**, and **HTTP API** for **API type**
	1. For **Security**, choose **Open**
	1. finish with **Add**

Now you can access the lambda function through the API Gateway.