import telebot



TOKEN = '1761778081:AAGRrFE1JeTeovQwNtA-eB7hW1HWbNJ9sa8'

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(content_types=['text'])
# def send_echo(message):
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")

bot.polling()
