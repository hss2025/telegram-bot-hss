import telegram.ext
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Bienvenue sur le bot HSS !")

if __name__ == '__main__':
    TOKEN = "7646509405:AAEPb86vBhJmszzdMBiDexrP5Sof_HSIiI8"
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
