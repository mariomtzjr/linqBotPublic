import logging
import json
import time

from telegram import InlineKeyboardButton, ReplyKeyboardMarkup
from telegram import (ParseMode, ChatAction)
from telegram.ext import ConversationHandler
from send_data import sendData


class Actions():

    def start(update, context):

        keyboard = [
            [
                InlineKeyboardButton("/log"),
                InlineKeyboardButton("/envio_cacre")
            ],
            [
                InlineKeyboardButton("/envio_saldos"),
            ]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            # one_time_keyboard=True,
            resize_keyboard=True
        )

        update.message.reply_text(
            text="""
            ¡Hola! Soy Crezebot,
            ¿Con qué puedo ayudarte?:
            """,
            reply_markup=reply_markup
        )

    def log(bot, update):
        logging.info({
            "process": "log",
            "user_id": update.message.from_user.id,
            "username": update.message.from_user.first_name,
            "text": update.message.text
        })

        keyboard = [
            [
                InlineKeyboardButton("/apli"),
                InlineKeyboardButton("/movimientos")
            ],
            [
                InlineKeyboardButton("/otros"),
                InlineKeyboardButton("/saldos")
            ]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            # one_time_keyboard=True,
            resize_keyboard=True
        )

        update.message.reply_text(
            text="¿Qué tipo de revisión deseas realizar?",
            reply_markup=reply_markup
        )

    def envio_cacre(bot, update):
        logging.info({
            "process": "envio_cacre",
            "user_id": update.message.from_user.id,
            "username": update.message.from_user.first_name,
            "text": update.message.text
        })

        update.message.reply_text(
            text="""
            Escribe CACRE#'CONTRATO1', 'CONTRATO2'
            """
        )

    def envio_saldos(bot, update):
        logging.info({
            "process": "envio_saldos",
            "user_id": update.message.from_user.id,
            "username": update.message.from_user.first_name,
            "text": update.message.text
        })

        update.message.reply_text(
            text="""
            Escribe SALDOS#
            """
        )

    def num_movimientos(bot, update):
        update.message.reply_text("Ingresa la fecha en formato AAAA/MM/DD.")

        logging.info({
            "process": "num_movimientos",
            "user_id": update.message.from_user.id,
            "username": update.message.from_user.first_name,
            "text": update.message.text
        })

    def apli(bot, update):
        logging.info({
            "process": "napli",
            "user_id": update.message.from_user.id,
            "username": update.message.from_user.first_name,
            "text": update.message.text
        })
        update.message.reply_text("Ingresa fecha en formato AAAA/MM/DD para ver registros APLI")

        text = update.message.text
        chat_id = update.message.chat_id

        if "/" in text:
            # Validar fecha
            bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
            time.sleep(0.3)

            response = sendData(text, "APLI")
            data = json.loads(response.text)

            """
            content = dict(zip([i for i in range(1, len(data)+1, 1)],data))
            content = {1: {dictionary}}
            """
            content = dict(zip([i for i in range(1, len(data)+1, 1)], data))

            bot.send_message(
                chat_id=chat_id,
                text="*Movimientos del dia*",
                parse_mode=ParseMode.MARKDOWN
            )
            for k, v in content.items():
                bot.send_message(
                    chat_id=chat_id,
                    text=v,
                    parse_mode=ParseMode.MARKDOWN
                )
