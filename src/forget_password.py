import time
import jwt

from utils import get_user_information
from utils import make_response_obj

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
