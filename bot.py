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
    kb.add(InlineKeyboardButton("Contact-us", callback_data="contact_us"))
    bot.send_message(message.chat.id,"Select lottery type", reply_markup=kb)
    pass

tickets = {
    "1": [2, 10],
    "2": [5, 20],
    "3": [9, 30]
}
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
        number = combo[-1]
        t = tickets[number]
        bot.edit_message_text(f"You have selected Combo {number} for {lottery.title()}\n\nThis combo includes {t[0]} {lottery.title()} tickets for the upcoming draw and is priced at ${t[1]}."
        , message.chat.id, message.id)

print("Started")
bot.infinity_polling()