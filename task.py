import logging
import time

from get_token_api import getToken
from xml.create_xml_cacre import createXMLC
from xml.create_xml_saldo import createXMLS
from execute import queryExecute
from telegram import (ParseMode, ChatAction)
from clean_data import cleanData
from send_data import sendData
from queries import queries


def detect_task(bot, update):

    text = update.message.text
    chat_id = update.message.chat_id

    token = getToken()

    logging.info({
        "process": "detect_task",
        "user_id": update.message.from_user.id,
        "username": update.message.from_user.first_name,
        "text": text
    })

    if "/" in text:
        bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        time.sleep(0.3)

        response = sendData(text, "")
        content = cleanData.cleanNMovimientos(response)
        bot.send_message(chat_id=chat_id, text=content, parse_mode=ParseMode.MARKDOWN)

        # bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
        # time.sleep(0.5)
        # response = sendData(text, "APLI")
        # content = cleanData.cleanMovimientos(response, bot, update)
    elif "#" in text:
        content = text.upper().split("#")
        oper = content[0]
        contracts = tuple(content[1].split(","))

        if oper == 'CACRE':
            query = queries.QueryL.queryD(contracts)
            createXMLC(queryExecute(query), token, bot, update)
        elif oper == 'SALDOS':
            query = queries.QueryL.querySaldo()
            createXMLS(queryExecute(query), token)

            bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
            time.sleep(0.3)

            bot.send_message(
                chat_id=chat_id,
                text="\
                    \n*Operación*: Envío de SALDOS:\
                    \n*Estatus*: Operación finalizada.",
                parse_mode=ParseMode.MARKDOWN
            )
