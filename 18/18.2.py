import requests
import json

# a = requests.get(
#     'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html'
# )  # делаем запрос на сервер по переданному адресу
# print(a.content)

# b = requests.get(
#     'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html'
# )
# print(b.status_code)  # узнаем статус полученного ответа

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ

# texts = json.loads(r.content) # делаем из полученных байтов python объект для удобной работы
# print(type(texts)) # проверяем тип сконвертированных данных
 
# for text in texts: # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')

# r = requests.get('https://api.github.com')
 
# d = json.loads(r.content) # делаем из полученных байтов python объект для удобной работы
 
# print(type(d))
# print(d['emails_url']) # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

# r = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
# print(r.content) # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет

# data = {'key': 'value'}
 
# r = requests.post('https://httpbin.org/post', json=json.dumps(data)) # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON 
# print(r.content)

def any_ipsum(x):
  r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
  return json.loads(r.content)[x]

print(any_ipsum(slice(1,-2)))
