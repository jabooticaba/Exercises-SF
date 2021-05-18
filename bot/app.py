import telebot



TOKEN = '1761778081:AAGRrFE1JeTeovQwNtA-eB7hW1HWbNJ9sa8'

bot = telebot.TeleBot(TOKEN)


keys = {'биткоин': 'BTC', 'эфириум':'ETH', 'доллар':'USD',}

# @bot.message_handler(content_types=['text'])
# def send_echo(message):
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['start', 'help'])
def start(message):  # Можно ввести message: telebot.types.Message
    text = 'Для начала работы введите команду в следующем формате: \n <имя валюты> ' \
           '<в какую перевести> <количество переводимой валюты> \n' \
           'Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

bot.polling()
