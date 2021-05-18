import telebot
import requests
import json


TOKEN = '1761778081:AAGRrFE1JeTeovQwNtA-eB7hW1HWbNJ9sa8'

bot = telebot.TeleBot(TOKEN)


keys = {'биткоин': 'BTC', 'эфириум':'ETH', 'доллар':'USD',}


class ConvertionException:
    pass



@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):  # Можно ввести message: telebot.types.Message
    text = 'Для начала работы введите команду в следующем формате: \n <имя валюты> ' \
           '<в какую перевести> <количество переводимой валюты> \n' \
           'Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) > 3:
        raise ConvertionException('Слишком много параметров')

    quote, base, amount = values

    if quote == base:
        raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f'Не удалось обработать валюту {quote}')

    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionException(f'Не удалось обработать валюту {base}')

    try:
        amount = float(amount)
    except ValueError:
        raise ConvertionException(f'Не удалось обработать количество {amount}')


    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.polling()
