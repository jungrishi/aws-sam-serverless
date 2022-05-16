import jwt

from db_models import get_user_by_id
from utils import make_response_obj

def password_reset_view_handler(event, context):
    print("Reset password lambda handler ...")

    token = event['pathParameters']['token']
    user_id = event['pathParameters']['user_id']
    
    # TODO: setup RDS and seed some user data
    user = get_user_by_id(user_id)

    if not user:
        return make_response_obj("user not found", 404)
    
    secret = f"{user['password_hash']}-{user['reset_link_timestamp']}"

    try:
        jwt.decode(token, secret, algorithms="HS256")
        return make_response_obj("Valid token, Render reset password page", 200)

    except jwt.ExpiredSignatureError as t_err:
        err_msg = str(t_err)
        return make_response_obj(f"Token Expired. {err_msg}", 400)

    except Exception as err:
        err_message = str(err)
        print(err_message)
        return make_response_obj(err_message, 400)

# print(password_reset_view_handler(None, None))