from recover_password import recover_password_handler
from utils import make_response_obj

from forget_password import forgot_password_handler
from reset_password import password_reset_view_handler

FORGET_PASSWORD = "forget_password"
RESET_PASSWORD = "reset_password"

def lambda_handler(event, context):
    route = event["path"]
    http_method = event["httpMethod"]

    # TODO: social login
    if "bearer token in header" == "true":
        return make_response_obj("Error", 403)
    
    # route handler
    if FORGET_PASSWORD in route:
        return forgot_password_handler(event=event, context=context)

    elif RESET_PASSWORD in route and http_method == "POST":
        return recover_password_handler(event, context)

    elif RESET_PASSWORD in route:
        return password_reset_view_handler(event=event, context=context)

    else:
        return make_response_obj(f"Route Not found {event}", 404)
