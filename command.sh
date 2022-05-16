# create an s3 bucket 
aws s3 mb s3://coding-task-bucket-sam

sam deploy

# delete
sam delete --stack-name ge-coding-task-sam