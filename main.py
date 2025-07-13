import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = os.environ["BOT_TOKEN"]
APP_URL = os.environ["APP_URL"]  # es. https://nome-bot.onrender.com

GIF_URL = "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif"

async def handle_buongiorno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "buongiorno":
        await update.message.reply_animation(GIF_URL)

async def handle_bro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "bro":
        with open("bro.jpg", "rb") as photo:
            await update.message.reply_photo(photo)

async def handle_pika(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pikachu! ⚡")

async def start_webhook():
    application = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("pika", handle_pika))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_buongiorno))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_bro))

    # Webhook
    await application.initialize()
    await application.start()
    await application.bot.set_webhook(f"{APP_URL}/webhook")
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        url_path="webhook",
        webhook_url=f"{APP_URL}/webhook",
    )

import asyncio
if __name__ == '__main__':
    asyncio.run(start_webhook())
