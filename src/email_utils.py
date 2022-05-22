import boto3
from botocore.exceptions import ClientError

def get_ses_client():
    return boto3.client("ses")

def send_email_via_ses(client: boto3.client, email_config: dict) -> None:
    try:
        RECIPENTS = email_config["to"]
        SENDER = email_config["from"]
        client.send_email(
            Destination={
                "ToAddresses": RECIPENTS,
            },
            Source=SENDER,
            Template="PasswordResetLink"
        )

    except ClientError as e:
        raise Exception()
    else:
        return
