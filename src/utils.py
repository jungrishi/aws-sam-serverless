import json

def make_response_obj(body):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "response ": body
        })
    }

def get_user_information(email):
    mock_db = [{'email': 'rishi', 'password': '123', 'id': 1}, {'email': 'jung', 'password': '456', 'id': 2}]
    for i in mock_db:
        if i['email'] == email:
            return i