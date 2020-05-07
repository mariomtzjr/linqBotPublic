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


def sendData(fecha, operacion):

    token = get_token.getToken()

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Bearer " + token['access_token']
    }

    if operacion == "":
        body = {
            "fideicomiso": fideicomiso,
            "fecha": fecha
        }
    else:
        body = {
                "fideicomiso": fideicomiso,
                "fecha": fecha,
                "operacion": operacion
            }

    response = createRequest(urlMov, headers, body)
    logging.info({
        "process": "sendData",
        "status": response,
        "message": response.text
    })
    return response

