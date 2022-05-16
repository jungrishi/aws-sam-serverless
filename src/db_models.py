from connection_manager import fetch_data 

def get_user_by_email(email):
    print('fetching user information by email ...')
    query = f'''select * from public.users where email = '{email}\''''
    data = fetch_data(query)
    if data:
        return data[0]
    return []

def get_user_by_id(id):
    print('fetching user information ...')
    query = f'''select * from public.users where id = '{id}\''''
    data = fetch_data(query)
    if data:
        return data[0]
    return []
