from db_models import get_user_by_id, update_user_password
from jwt_utils import jwt_decode_token
from utils import JWTException, make_response_obj

def recover_password_handler(event, context):
    print("Recover password lambda handler ...")

    token = event['requestBody']['token']
    user_id = event['requestBody']['user_id']
    new_password_hash = event['requestBody']['passwordHash']
    
    # TODO: setup RDS and seed some user data
    user = get_user_by_id(user_id)

    if not user:
        return make_response_obj("user not found", 404)
    
    secret = f"{user['password_hash']}-{user['reset_link_timestamp']}"

    try:
        jwt_decode_token(token, secret)
        update_user_password(user_id, new_password_hash)
    except JWTException as err:
        return make_response_obj(str(err))
    except Exception as err:
        return make_response_obj(str(err))
