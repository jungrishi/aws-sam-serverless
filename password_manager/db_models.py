from connection_manager import fetch_one, write_to_db
from password_manager.logger_utils import get_logger

logger = get_logger()

def get_user_by_email(email: str) -> dict:
    logger.info('fetching user information by email ...')
    query = f'''select * from public.users where email = '%s;'''
    return fetch_one(query, [email])

def get_user_by_id(id: int) -> dict:
    logger.info('fetching user information by id ...')
    query = f'''select * from public.users where id = %s;'''
    return fetch_one(query, [id])

def update_user_reset_time(user_id: int, epoch_time: int):
    return write_to_db(f'''update users set reset_link_timestamp = %s where id = %s;''', (epoch_time, user_id))

def update_user_password(user_id: int, password_hash: int):
    return write_to_db(f'''update users set password_hash = %s where id = %s;''', (password_hash, user_id))
