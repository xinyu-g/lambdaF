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

## 8. Add HTTP API Gateway

	1. Under **Functional overview**, choose **Add trigger** 
	1. choose the lambda function
	1. select **API Gateway**
	1. choose **Create an API**, and **HTTP API** for **API type**
	1. For **Security**, choose **Open**
	1. finish with **Add**

## 9. Add REST API (Alternative)

1. Under **Functional overview**, choose **Add trigger** 
 2. choose the lambda function
 3. select **API Gateway**
 4. choose **Create an API**, and **REST API** for **API type**
 5. For **Security**, choose **Open**
 6. finish with **Add**
 7. Navigate to **API Gateway** service, click on the rest api just created
 8. In **Resources** tab, in the **Actions** menu, choose **Create method** 
 9. Choose **GET** from the dropdown menu
 10. Leave the **Integration type** set to **Lambda Function**
 11. In the **Lambda Function** field, type in the name of the lambda function
 12. Choose **Save**
 13. Choose **Deploy API** from the **Actions** dropdown menu
 14. For **Deployment stage**, choose **[new stage]**
 15. For **Stage name**, enter 'xxx'
 16. Choose **Deploy**
 17. Go to the **Stages** tab and find the **Invoke URL** /base url
 18. Alternatively, Go back to the lambda to find the url under Functional overview

