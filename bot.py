import requests
import json
import logging
import actions
import tokenBot
import task

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = tokenBot.setToken()

response = requests.get("https://api.telegram.org/bot"+token+"/getMe")
res = json.loads(response.text)


def main():
    """Start the bot.
    Command: /start
    """

    updater = Updater(token, use_context=True)

    # Dispatcher
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", actions.Actions.start))
    dp.add_handler(CommandHandler("log", actions.Actions.log))
    dp.add_handler(CommandHandler("movimientos", actions.Actions.num_movimientos))
    dp.add_handler(CommandHandler("apli", actions.Actions.apli))
    dp.add_handler(CommandHandler("envio_cacre", actions.Actions.envio_cacre))
    dp.add_handler(CommandHandler("envio_saldos", actions.Actions.envio_saldos))

    dp.add_handler(MessageHandler(
        Filters.regex("\d\d\d\d/\d\d/\d\d"),
        task.detect_task
        )
    )
    dp.add_handler(MessageHandler(
        Filters.regex("[A-Za-z]+#[0-9a-zA-Z,]+|[A-Za-z]+#[0-9a-zA-Z,]*"),
        task.detect_task
        )
    )

    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':

    logging.basicConfig(
        format='%(asctime)s: %(name)s - %(levelname)s: %(message)s',
        level=logging.INFO
    )
    main()
