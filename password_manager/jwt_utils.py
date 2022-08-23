import jwt

from utils import JWTException

ALGORITHM = "HS256"

def is_valid_token(token: str, secret: str) -> bool:
    payload = jwt_decode_token(token, secret)
    if payload:
        return True
    return False


def jwt_decode_token(token: str, secret: str) -> dict:
    """
    Return the payload of the token
    """
    try:
        payload = jwt.decode(token, secret, algorithms=ALGORITHM)
        return payload

    except jwt.ExpiredSignatureError as t_err:
        err_message = str(t_err)
        raise JWTException(f"{err_message}")

    except Exception as err:
        err_message = str(err)
        raise JWTException(f"{err_message}")

def jwt_generate_token(payload: dict, secret: str) -> str:
    """
    Generates a unique token for the given payload and secret
    """
    try:
        return jwt.encode(payload, secret, algorithm=ALGORITHM)
    except Exception as err:
        print(err)
        return None
