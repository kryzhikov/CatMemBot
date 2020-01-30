import logging
from text_on_photo import get_mem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Отправь подпись, получи картинку с котом и твоей подписью!\nНе понравилось? Попробуй еще 😎')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def send_mem(update, context):
    text = update.message.text
    logger.info(text)
    get_mem(text)
    update.message.reply_photo(photo = open("./sample-out.jpg", "rb")) 

def main():

    updater = Updater("965990520:AAEme0jNGO_Ing2QIo8IGeU-GjDmsilcLh8", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, send_mem))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()