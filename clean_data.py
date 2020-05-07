import json
from telegram import ParseMode


class cleanData():

    def cleanNMovimientos(response):

        data = json.loads(response.text)

        content = "\
            Total de movimientos:\
            \n*ALTA*: {},\
            \n*APLI*: {},\
            \n*CACRE*: {},\
            \n*OTROS*: {},\
            \n*SALDO*: {},\
            ".format(
                data["ALTA"],
                data["APLI"],
                data["CACRE"],
                data["OTROS"],
                data["SALDO"])

        return content

    def cleanMovimientos(response, bot, update):
        chat_id = update.message.chat_id

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
