import json

print("Loading function...")

def response_obj(body):
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps({"response": body})
    return responseObject

def forgot_password_handler(message, context):
    # print("Received event: " + json.dumps(event, indent=2))
    
    return response_obj("Email send with password reset link")
