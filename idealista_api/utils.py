import base64
import requests


def get_bearer_token(api_key: str, secret: str) -> str:
    """Request a Bearer token for OAuth authentication.

    Args:
        api_key (str): API key
        secret (str): secret
    """
    credentials = encode_values(api_key + ":" + secret)
    req = requests.post(
        "https://api.idealista.com/oauth/token",
        "grant_type=client_credentials&scope=read",
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    ).json()
    return req["access_token"]


def encode_values(credentials: str):
    """[summary]

    Args:
        credentials (str): API key and secret concatenated with a ':' character
    """

    base64_bytes = base64.b64encode(credentials.encode("ascii"))
    return base64_bytes.decode("ascii")
