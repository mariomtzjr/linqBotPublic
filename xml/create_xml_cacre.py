import logging
import time

from requirements.req_cacre import cacre
from send_data import sendData
from telegram import (ParseMode, ChatAction)


def createXMLC(result_cacre, token, bot, update):
    chat_id = update.message.chat_id

    logging.info({
        "process": "createXMLC",
        "message": "Creating xmls"
    })

    for row in result_cacre:
        xml_cacre = cacre(row)

        """
        Envío de xmls a la API de Linq
        """
        response = sendData(xml_cacre, token)
        bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        time.sleep(0.3)

        bot.send_message(
            chat_id=chat_id,
            text="*{}*".format(response.text),
            parse_mode=ParseMode.MARKDOWN
        )
