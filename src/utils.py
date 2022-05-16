import json
import connection_manager 

def make_response_obj(body, status_code=200):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "response ": body
        })
    }


def get_user_by_email(email):
    print('fetching user information by email ...')
    query = f'''select * from public.users where email = '{email}\''''
    data = connection_manager.fetch_data(query)
    if data:
        return data[0]
    return []

def get_user_by_id(id):
    print('fetching user information ...')
    query = f'''select * from public.users where id = '{id}\''''
    data = connection_manager.fetch_data(query)
    if data:
        return data[0]
    return []