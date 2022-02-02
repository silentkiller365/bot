import os
import telebot


bot = telebot.TeleBot("5117499847:AAHr9by8LAI2m15TWZrBSEnn8WpwEe9-EWs")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm test#")


@bot.message_handler(commands=["ssh"])
def send_message(message):
  bot.send_message(message.chat.id, "connecting to the sever☁️")



bot.polling()
