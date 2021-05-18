import telebot

from config import keys, TOKEN

from utils import CryptoConverter, ConvertionException



bot = telebot.TeleBot(TOKEN)

# bot.delete_webhook() - раскомментить при ошибке вебхука




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
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Неправильное количество параметров')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
