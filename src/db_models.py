from typing import List
from connection_manager import fetch_data, insert_data

def get_user_by_email(email: str) -> List[dict]:
    print('fetching user information by email ...')
    query = f'''select * from public.users where email = '{email}\''''
    data = fetch_data(query)
    if data:
        return data[0]
    return []

def get_user_by_id(id: int) -> List[dict]:
    print('fetching user information ...')
    query = f'''select * from public.users where id = '{id}\''''
    data = fetch_data(query)
    if data:
        return data[0]
    return []

def update_user_reset_time(user_id: int, epoch_time: int) -> bool:
    query = f'''update users set reset_link_timestamp = %s where user_id = %s;'''
    return insert_data(query, (epoch_time, user_id))
