import json
import connection_manager 

def make_response_obj(body):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "response ": body
        })
    }

def get_user_information(email):
    print('fetching user information ...')
    query = f'''select * from public.users where email = '{email}\''''
    data = connection_manager.fetch_data(query)
    print(data)
    if data:
        return data[0]
    return []