# create an s3 bucket 
aws s3 mb s3://coding-task-bucket-sam

#package configuration
sam package --s3-bucket coding-task-bucket-sam --template-file template.yaml --output-template-file gen/output-template.yaml

# deploy
sam deploy --template-file gen/output-template.yaml --stack-name ge-coding-task-sam --capabilities CAPABILITY_IAM

# delete
sam delete --stack-name ge-coding-task-sam