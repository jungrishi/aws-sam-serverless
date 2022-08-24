import pytest
from tests.utils.fixtures import parse_connection_str


def test_parse_connection_str():
    # given
    db_string = 'getemails:password456@localhost:5432/nice_db'
    expected = {
        'user': 'getemails',
        'password': 'password456',
        'host': 'localhost',
        'port': 5432,
        'database': 'nice_db'
    }
    # when
    actual = parse_connection_str(db_string)
    # then
    assert expected == actual


def test_parse_connection_str__should_throw_exception():
    # given
    db_string = 'returnalyze:password456@K1-east.co/nice_db'
    # when
    with pytest.raises(Exception) as e:
        parse_connection_str(db_string)
