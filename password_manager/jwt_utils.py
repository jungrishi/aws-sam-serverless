import jwt

from utils import JWTException

ALGORITHM = "HS256"

def is_valid_token(token: str, secret: str) -> bool:
    return True if decode(token, secret) else False

def decode(token: str, secret: str, algorithms=ALGORITHM) -> dict:
    """Verifies a JWT string's signature and validates payload

    Args:
        token (str): A signed JWT Token to be verified
        secret (str): the secret to use for signing the payload
        algorithm (str, optional): The algorithm to use for signing the payload. Defaults to HS256.

    Returns:
        dict: The dict representation of the claims set, assuming the signature is valid and all requested data validation passes.
    """
    try:
        return jwt.decode(token, secret, algorithms=algorithms)
    except jwt.ExpiredSignatureError as t_err:
        err_message = str(t_err)
        raise JWTException(f"{err_message}")

def encode(payload: dict, secret: str, algorithm: str = ALGORITHM) -> str:
    """
    Encodes a claims set and returns a JWT string.

    Generates a unique token for the given payload and secret
    Args:
        payload (dict): data
        secret (str): the secret to use for signing the payload
        algorithm (str, optional): The algorithm to use for signing the payload. Defaults to HS256.
    
    Returns:
        str: The string representation of the header, payload, and signature.
    """
    return jwt.encode(payload, secret, algorithm=algorithm)
