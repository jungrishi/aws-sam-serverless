import random
from unittest.mock import mock_open

THRESHOLD = 0.5
MIN_DATA_LEN = 10
def lambda_handler(event, context):
    # check system capacity
    poll_system_capacity = random.random()
    if THRESHOLD > poll_system_capacity:
        return {
            "continue": False,
            "done": False,
        }

    # get data from db
    datas = get_records_from_db()

    if len(datas) < MIN_DATA_LEN:
        return {
            "continue": False,
            "data": [],
            "done": True
        }

    splitted_data = [datas[i:i+MIN_DATA_LEN] for i in range(0, len(datas), MIN_DATA_LEN)]
    return {
        "continue": True,
        "done": False,
        "data": splitted_data
    }
