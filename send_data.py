import os
import logging
import get_token

from dotenv import load_dotenv
from settings import path_dir_env
from create_request import createRequest

load_dotenv(os.path.join(path_dir_env, '.env'))

urlMov = os.getenv("APIMOVURL")
fideicomiso = os.getenv("FIDEICOMISO")
urlAlta = os.getenv("APIALTAURL")


def sendData(xml, token):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Bearer " + token['access_token']
    }

    body = {
        "fideicomiso": fideicomiso,
        "xml": xml
    }

    response = createRequest(urlAlta, headers, body)

    if response.status_code == 401:
        logging.info({
            "process": "sendData",
            "status": response,
            "message": "Generating new token"
        })
        token2 = get_token.getToken()
        sendData(xml, token2)
    else:

        logging.info({
            "process": "sendData",
            "status": response,
            "message": response.text
        })

    return response
