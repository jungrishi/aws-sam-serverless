import os
from typing import Iterable, List
import psycopg2
from psycopg2.extras import DictCursor

from password_manager.logger_utils import get_logger

logger = get_logger()

#  TODO: get the config from the env
db_config = {
    "dbname": os.environ.get("DBNAME", "ge_coding_task"),
    "user": os.environ.get("DBUSER", "rishi"),
    "password": os.environ.get("DBPASSWORD", "password"),
    "host": os.environ.get("DBENDPOINT", "127.0.0.1"),
    "port": os.environ.get("DBPORT", 5432),
}

def get_connection():
    return psycopg2.connect(
        dbname=db_config["dbname"],
        user=db_config["user"],
        password=db_config["password"],
        host=db_config["host"],
        port=db_config["port"],
    )

def fetch_one(query: str, params: list) -> dict:
    """fetch single record from the database.
    
    Connects to database and executes the query to return a single record. 

    Args:
        query (str): SQL to execute.
        values (str): values to filter.
    """
    connection = get_connection()
    try:
        with connection.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, params)
            breakpoint()
            result_set = cur.fetchone()
            to_dict(result_set)

    except psycopg2.OperationalError as Operror:
        connection.rollback()
        logger.exception("Database error")
        raise
    finally:
        connection.close()

def write_to_db(query: str, values: tuple):
        """Execute and commit query interpolating the values.
        Args:
            query (str): SQL to execute.
            values (str): values to write.
        """
        connection = get_connection()
        try:
            with connection.cursor() as cur:
                cur.execute(query, values)
                connection.commit()
                return
        except psycopg2.Error:
            connection.rollback()
            logger.exception("Database error")
            raise
        finally:
            connection.close()

def to_dict(result: Iterable) -> dict:
    """Returns a list.

    Converts the db result to corresponding key(column_name) value(column_value) pair.
    """
    return [{k: v} for k, v in result.items()][0]
