import boto3

client = boto3.client('stepfunctions')

THRESHOLD = 0.5
def lambda_handler(event, context):
    StateMachineArn = event.restart.StateMachineArn
    client.start_execution(
        stateMachineArn=StateMachineArn,
        name='string',
        input='{}',
        traceHeader='string'
    )
