import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# URL della GIF che vuoi inviare
GIF_URL = "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "buongiorno":
        await update.message.reply_animation(GIF_URL)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.run_polling()