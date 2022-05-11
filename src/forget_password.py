import json
import time
import jwt

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

def forgot_password_handler(message, context):
    # forget password handler ...
    print("Executing forget password lambda handler ...")

    # get timestamp and email address from header
    req_timestamp_epoch = time.time()
    user_email = message.get('email', 'rishi')
    
    
    # get user info for the email address from RDS
    # TODO: setup RDS and seed some user data
    user = get_user_information(user_email)

    # use password and the timestamp as a secret key for the jWT
    payload = {'email': user_email, 'timestamp': req_timestamp_epoch}
    
    # user password makes this a one-time-use token by adding current user password as one of secret key
    # request timestamp makes JWT generate unique token when same user makes request multiple times
    secret = f"{user['password']}-{req_timestamp_epoch}" 
    
    encoded_token = jwt.encode(payload, secret, algorithm="HS256")
    
    return make_response_obj(f"Email send password reset link. token: {encoded_token}")

print(forgot_password_handler({'email': 'rishi'}, None))
