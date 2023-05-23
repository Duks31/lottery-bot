from telebot import TeleBot
from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import os, dotenv

bot_token = os.getenv("bot_token")
bot = TeleBot(bot_token, parse_mode="HTML")

@bot.message_handler(["start"])
def start(message):
    # Start message
    pass

print("Started")
bot.infinity_polling()