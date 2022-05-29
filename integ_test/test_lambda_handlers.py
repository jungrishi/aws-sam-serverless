import json
from integ_test.utils.fixtures import *
from src.forgot_password import forgot_password_handler

test_params = [
    ("123.com", {"response": "user not found", "status": 404}),
    ("ranabhat.85@gmail.com", {"response": "Email send password reset link", "status": 200})
    ]

@pytest.mark.parametrize("email, expected", test_params)
def test_forget_password_status(dbsession_pg, email, expected):
    response = forgot_password_handler({"queryStringParameters": {"email": email}}, {})
    assert response["statusCode"] == expected["status"]

@pytest.mark.parametrize("email, expected", test_params)
def test_forget_password_response(dbsession_pg, email, expected):
    response = forgot_password_handler({"queryStringParameters": {"email": email}}, {})
    body = json.loads(response["body"])

    assert f'{expected["response"]}' in body["response"]
