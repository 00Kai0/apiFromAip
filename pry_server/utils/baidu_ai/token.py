import requests
from . import config


def get_access_token(client_id, client_secret):
    '''
    获取access_token
    '''
    request_url = config.token_url

    payload = {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}

    response = requests.post(url=request_url, params=payload)
    content = response.json()
    return content['access_token']
