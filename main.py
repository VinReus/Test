import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from aiohttp import web

GIF_URL = "https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif"

async def handle_buongiorno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "buongiorno":
        await update.message.reply_animation(GIF_URL)

async def handle_bro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "bro":
        with open("gaetanoamabile_14040423_232615864.jpg", "rb") as photo:
            await update.message.reply_photo(photo)

async def handle_pika(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pikachu! ⚡")

async def start_bot():
    TOKEN = os.environ["BOT_TOKEN"]
    APP_URL = os.environ["APP_URL"]

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("pika", handle_pika))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_buongiorno))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_bro))

    async def webhook_handler(request):
        data = await request.json()
        update = Update.de_json(data, app.bot)
        await app.update_queue.put(update)
        return web.Response()

    async def on_startup(app_):
        await app.bot.set_webhook(f"{APP_URL}/webhook")

    web_app = web.Application()
    web_app.add_routes([web.post("/webhook", webhook_handler)])
    web_app.on_startup.append(on_startup)

    await app.initialize()
    await app.start()
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.environ.get("PORT", 10000)))
    await site.start()

    print("Bot in ascolto su /webhook...")

    # Rimani attivo
    await app.updater.start_polling()  # oppure await asyncio.Event().wait() per tenerlo attivo

import asyncio
if __name__ == '__main__':
    asyncio.run(start_bot())
    
