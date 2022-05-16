from utils import make_response_obj

from forget_password import forgot_password_handler
from reset_password import password_reset_view_handler

def lambda_handler(event, context):
    route = event["path"]
    http_method = event["httpMethod"]
    
    # route handler
    if route == "forget_password":
        return forgot_password_handler(event=event, context=context)
    
    elif "reset_password/" in route:
        return password_reset_view_handler(event=event, context=context)
    
    return make_response_obj("Route Not found", 404)
