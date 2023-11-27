
import telebot

bot = telebot.TeleBot("Your_Token_Bot")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "خوش آمدید📸")

bot.polling()
