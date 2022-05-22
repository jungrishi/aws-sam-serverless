import json
from requests_toolbelt.multipart import decoder

def make_response_obj(body, status_code=200):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "response ": body
        })
    }

def lambda_handler(event, context):
    json_body = event['body-json']
    data = json_body.split("\n")
    return make_response_obj(f'Hello from Lambda!{data}')
