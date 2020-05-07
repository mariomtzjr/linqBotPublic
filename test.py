from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler

TELEGRAM_HTTP_API_TOKEN = '851081714:AAG5Ac8VRmw9HTZ379966gjWdE7dS4Emqf4'

FIRST, SECOND = range(2)


def start(bot, update):
    keyboard = [
            [
                InlineKeyboardButton("/apli", callback_data=str(FIRST)),
                InlineKeyboardButton("/movimientos")
            ],
            [
                InlineKeyboardButton("/otros"),
                InlineKeyboardButton("/saldos")
            ]
        ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text(
        u"Start handler, Press next",
        reply_markup=reply_markup
    )
    return FIRST


def first(bot, update):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Next", callback_data=str(SECOND))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="First CallbackQueryHandler, Press next"
    )

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.edit_message_reply_markup(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        reply_markup=reply_markup
    )
    return SECOND


def second(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text=u"Second CallbackQueryHandler"
    )
    return

updater = Updater(TELEGRAM_HTTP_API_TOKEN)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        FIRST: [CallbackQueryHandler(first)],
        SECOND: [CallbackQueryHandler(second)]
    },
    fallbacks=[CommandHandler('start', start)]
)

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()

updater.idle()
