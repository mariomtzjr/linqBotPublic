import json
import os

from dotenv import load_dotenv
from settings import path_dir_env
from create_request import createRequest

load_dotenv(os.path.join(path_dir_env, '.env'))


def getToken():
    urlLogin = os.getenv("APILOGINURL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    body = {
        "username": username,
        "password": password
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = createRequest(urlLogin, headers, body)

    jsonResponse = json.loads(response.text)

    return jsonResponse
