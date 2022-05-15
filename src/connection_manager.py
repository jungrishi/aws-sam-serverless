import psycopg2
from psycopg2.extras import DictCursor

#  TODO: get the config from the env
db_config = {
    "dbname": "ge_coding_task",
    "user": "rishi",
    "password": "password",
    "host": "localhost",
    "port": "5432",
}

def get_connection():
    return psycopg2.connect(
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config["port"],
    )


def fetch_data(query):
    # Note: connection pool
    connection = get_connection()

    try:
        with connection.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query)
            result = cur.fetchall()
            return to_dict(result)

    except Exception as error:
        print(error)
        return []


def to_dict(result):
    """Returns a list

    Converts the db result to corresponding key(column_name) value(column_value) pair
    """
    arr = []
    for x in result:
        obj={}
        for k, v in x.items():
            obj[k] = v
        arr.append(obj)

    return arr
