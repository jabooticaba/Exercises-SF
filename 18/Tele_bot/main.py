# pip3 install pyTelegramBotAPI

import telebot
 
TOKEN = "1433434693:AAGSo26QPwf5sBuraSTV4wAjo7JPziIz2Vk"
 
bot = telebot.TeleBot(TOKEN)
# Чтобы запустить бота, нужно воспользоваться методом polling.

bot.polling(none_stop=True)

# @bot.message_handler(content_types=['voice, '])
# def repeat(message: telebot.types.Message):
#     bot.send_message (message.chat.id , "У тебя красивый голос!")

# Ответ на сообщение /start, /help

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")


# Ответ на сообщение с картинкой:

@bot.message_handler(content_types=['photo, '])
def send_ansver(message):
    bot.reply_to(message.chat.id , "Nice meme XDD")

# @bot.message_handler(content_types=['photo', ]) # Эталон ответа
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')