import json

from db_models import get_user_by_id, update_user_password
from jwt_utils import is_valid_token
from utils import make_response_obj
from password_manager.logger_utils import get_logger

logger = get_logger()

def recover_password_handler(event, context):
    logger.info("Recover password lambda handler ...")

    decoded_body = json.loads(event['body'])
    token = decoded_body['token']
    user_id = decoded_body['user_id']
    new_password_hash = decoded_body['passwordHash']
    
    user = get_user_by_id(user_id)

    if not user:
        return make_response_obj("user not found", 404)
    
    secret = f"{user['password_hash']}-{user['reset_link_timestamp']}"

    if is_valid_token(token, secret):
        update_user_password(user_id, new_password_hash)
        return make_response_obj("Successful password reset")
    else:
        return make_response_obj("Invalid token", 403)
