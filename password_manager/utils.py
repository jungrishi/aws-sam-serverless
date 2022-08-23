import json

class JWTException(Exception):
    pass

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
