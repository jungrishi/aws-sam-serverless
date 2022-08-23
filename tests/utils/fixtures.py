import os
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from testcontainers.postgres import PostgresContainer

from integ_test.utils.pg_data.data import insert_data
from integ_test.utils.pg_data.ddl import create_required_tables

def parse_connection_str(db_string):
    try:
        import re
        # expected pattern {user}:{password}@{account}/{database}/{warehouse}
        p = re.compile('(.*):(.*)@(.*):(.*)/(.*)')
        result = p.search(db_string)

        conn_info = {
            'user': result.group(1),
            'password': result.group(2),
            'host': result.group(3),
            'port': int(result.group(4)),
            'database': result.group(5),
        }

        return conn_info
    except:
        raise Exception('Invalid input string format', db_string)

def add_to_env(conn):
    os.environ['DBNAME'] = conn['database']
    os.environ['DBPASSWORD'] = conn['password']
    os.environ['DBENDPOINT'] = conn['host']
    os.environ['DBUSER'] = conn['user']

@pytest.fixture(scope='session')
def engine_pg():
    with PostgresContainer('postgres:9.5') as postgresql:
        db_connection_string = postgresql.get_connection_url()
        conn_info = parse_connection_str(db_connection_string)

        add_to_env(conn_info)
        pg_engine = create_engine(db_connection_string)
        yield pg_engine


@pytest.fixture(scope='session')
def dbsession_pg(engine_pg):
    connection = engine_pg.connect()

    Session = sessionmaker(engine_pg)

    session = Session()

    initialize_db(session)

    yield session

    session.close()
    connection.close()

def initialize_db(session: Session):
    """
    Initializes data for postgres required for integration tests.
    """
    try:
        create_required_tables(session)
        insert_data(session)
    except:
        session.rollback()
        raise
    else:
        session.commit()
