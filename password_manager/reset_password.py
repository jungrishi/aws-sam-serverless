from db_models import get_user_by_id
from jwt_utils import jwt_decode_token
from utils import JWTException, make_response_obj

from password_manager.logger_utils import get_logger

logger = get_logger()

def password_reset_view_handler(event, context):
    logger.info("Reset password lambda handler ...")

    token = event['pathParameters']['token']
    user_id = event['pathParameters']['user_id']
    
    # TODO: setup RDS and seed some user data
    user = get_user_by_id(user_id)

    if not user:
        return make_response_obj("user not found", 404)
    
    secret = f"{user['password_hash']}-{user['reset_link_timestamp']}"

    try:
        jwt_decode_token(token, secret)
        return make_response_obj("Valid token, Render reset password page", 200)
    except JWTException as err:
        return make_response_obj(str(err), 400)
