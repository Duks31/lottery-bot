from telebot import TeleBot
from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import os, dotenv

dotenv.load_dotenv()
bot_token = os.getenv("bot_token")
bot = TeleBot(bot_token, parse_mode="HTML")

@bot.message_handler(["start"])
def start(message):
    
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("PowerBall", callback_data="powerball"), InlineKeyboardButton("Megamillions", callback_data = "megamillions"))
    bot.send_message(message.chat.id,"Select lottery type", reply_markup=kb)
    pass


@bot.callback_query_handler(lambda call: call.data)
def callback_handler(callback: CallbackQuery):
    message = callback.message
    if callback.data in ["powerball", "megamillions"]:
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("Combo 1", callback_data="combo_1:"+ callback.data), InlineKeyboardButton("Combo 2", callback_data="combo_2:"+ callback.data))
        kb.add(InlineKeyboardButton("Combo 3", callback_data="combo_3:"+ callback.data))
        bot.edit_message_text("Which combo do you want? ",message.chat.id, message.id, reply_markup=kb)

    if callback.data.startswith("combo"):
        combo, lottery = callback.data.split(":")
        numnber = combo[-1]
        bot.edit_message_text("You have selected Combo {} for {}".format(numnber, lottery), message.chat.id, message.id)


print("Started")
bot.infinity_polling()