import json
from requests_toolbelt import MultipartDecoder
import base64

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

FILE_HEADERS = {
    "first_name": {type: "str"},
    "last_name": {type: "str"},
    "domain": {type: "str"},
    "company": {type: "str"},
}

def lambda_handler(event, context):
    body = event['body']

    content_type = event['headers']['Content-Type']
    content = base64.b64decode(body)

    decoder = MultipartDecoder(content, content_type)
    
    rows = []
    headers = []
    for i, part in enumerate(decoder.parts):
        if i == 0:
            headers = part.text.split(",")
            for j in headers:
                if j.lower() not in list(FILE_HEADERS.values()):
                    return make_response_obj("Invalid file headers", 400)
        else:
            row = part.text.split(",")
            rows.append(row)

    if len(rows) < 10:
        return make_response_obj("records should greater or equal to 10", 400)

    return make_response_obj(f'Hello from Lambda! {rows}')
