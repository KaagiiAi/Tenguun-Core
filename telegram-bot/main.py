import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import json
import os

memory = {}

def save_message(user_id, message):
    if str(user_id) not in memory:
            memory[str(user_id)] = []
                memory[str(user_id)].append(message)
                    with open("memory.json", "w", encoding="utf-8") as file:
                            json.dump(memory, file, ensure_ascii=False, indent=2)

                            def generate_chatgpt_style_response(user_id, user_text):
                                save_message(user_id, user_text)
                                    return f"🤖 Хэрэглэгч {user_id}-д хариу: {user_text[::-1]}"

                                    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                        user_id = update.effective_user.id
                                            user_text = update.message.text
                                                response = generate_chatgpt_style_response(user_id, user_text)
                                                    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

                                                    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

                                                    app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
                                                    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
                                                    app.run_polling()