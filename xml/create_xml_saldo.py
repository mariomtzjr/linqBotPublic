import logging

from requirements.req_saldo import saldo
from send_data import sendData


def createXMLS(result_saldo, token):

    logging.info({
        "process": "createXMLS",
        "message": "Creating xmls"
    })

    for row in result_saldo:
        xml_saldo = saldo(row)

        """
        Envío de xmls a la API de Linq
        """
        sendData(xml_saldo, token)
