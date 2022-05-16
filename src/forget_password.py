from datetime import datetime, timezone, timedelta

import jwt

from utils import make_response_obj
from utils import get_user_by_email

def forgot_password_handler(event, context):
    # forget password handler ...
    print("Executing forget password lambda handler ...")

    epoch_timestamp_now = datetime.now(tz=timezone.utc)
    expire_timestamp_epoch = epoch_timestamp_now + timedelta(days=2)
    
    query_params = event["queryStringParameters"]
    user_email = query_params.get('email', None)
    domain_url = context['domainName']
    if not user_email:
        return make_response_obj("email not found", 400)
    
    # get user info for the email address from RDS
    # TODO: setup RDS and seed some user data
    user = get_user_by_email(user_email)

    if not user:
        return make_response_obj("user not found", 404)

    # use password and the timestamp as a secret key for the jWT
    payload = {'email': user_email, 'exp': expire_timestamp_epoch}
    
    # user password makes this a one-time-use token by adding current user password as one of secret key
    # epoch timestamp makes JWT generate unique token when same user makes request multiple times
    secret = f"{user['password_hash']}-{epoch_timestamp_now}"
    
    encoded_token = jwt.encode(payload, secret, algorithms="HS256")

    reset_link = f"{domain_url}/resetpassword/{user['id']}/{encoded_token}"

    # send token to the email server
    # save token_created_at
    return make_response_obj(f"Email send password reset link. token: {reset_link}")

# print(forgot_password_handler({"queryStringParameters": {"email": "ranabhat.85@gmail.com"}}, {'domainName': "localhost"}))