
import telebot

bot = telebot.TeleBot("6829954845:AAHG60sdnxkgPR5uOQHROkAUfcCPAPfRbH4")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "خوش آمدید📸")

bot.polling()