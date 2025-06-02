from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import logging
import os
from logic import generate_response
from config import TELEGRAM_BOT_TOKEN

# Лог тохиргоо
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Мессеж хүлээн авагч функц
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text
    response = generate_response(user_id, user_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Апп эхлүүлэх
app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
