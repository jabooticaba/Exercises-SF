import redis
import json

red = redis.Redis(
  host='redis-11669.c73.us-east-1-2.ec2.cloud.redislabs.com',
  port=11669, # порт подключения. На локальной машине это должно быть 6379.
  password='BY2iL2SNA2X4C8jObOpnGPvQ0F9HPxqP' # для локальной машины пароль не требуется. Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password.
)


# red.set('var1', 'value1') # записываем в кеш строку "value1"
# print(red.get('var1')) # считываем из кэша данные


# dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи
# red.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку
# converted_dict = json.loads(red.get('dict1')) # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
# print(type(converted_dict)) # убеждаемся, что получили действительно словарь
# print(converted_dict) # ну и выводим его содержание

'''Напишите программу, которая будет записывать и кэшировать номера ваших друзей. Программа должна уметь воспринимать несколько команд: записать номер, показать номер друга в консоли при вводе имени или же удалить номер друга по имени. Кэширование надо производить с помощью Redis. Ввод и вывод информации должен быть реализован через консоль (с помощью функций input() и print()).'''


def new_friend(name, number):
  red.set(name, number)
  return f'Запись {name}:{number} создана'

def show_number(name):
  print(red.get(name))


while True:
  x = input("Введите команду: new, show, exit")

  if x == 'new':
    new_friend(input("Введите имя друга: "), input('Введите номер друга: '))

  if x == 'show':
    show_number(input('Введите имя друга: '))

  if x == 'exit':
    break

  else:
    print("Введена неверная команда")