import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# URL della GIF
GIF_URL = "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif"

# Funzione per rispondere a "Buongiorno"
async def handle_buongiorno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "buongiorno":
        await update.message.reply_animation(GIF_URL)

# Funzione per rispondere a "Bro" con una foto
async def handle_bro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "bro":
        with open("gaetanoamabile_14040423_232615864.jpg", "rb") as photo:
            await update.message.reply_photo(photo)

# Comando /Pika
async def handle_pika(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pikachu! ⚡")

# MAIN
if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()

    # Aggiungi i singoli handler
    application.add_handler(CommandHandler("pika", handle_pika))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_buongiorno))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_bro))

    application.run_polling()
