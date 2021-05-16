# pip3 install beautifulsoup4
# pip3 install lxml

from bs4 import BeautifulSoup
import requests

def main():  # Парсинг вопросов с главной страницы  и ссылок на них
  base = 'https://ru.stackoverflow.com'  # Сайт, на котором проводится поиск
  html = requests.get(base).content  # Загрузка html-кода страницы
  soup = BeautifulSoup(html, 'lxml')  # Конструктор BeautifulSoup получает 2 аргумента: готовый html от requests.get  и алгоритм, по коротому будем парсить (от библиотеки lxml) 
  div = soup.find('div', id = 'question-mini-list')  # Поиск нужного контейнера
  a = div.find_all('a', class_ = 'question-hyperlink')  # Поиск всех блоков с классом "question-hyperlink"


  for _ in a:  # Цикл по всем блокам
    print(_.getText(), base + _.get('href'))  # Взятие текста методом getText, взятие ссылки путём обращения к атрибуту 'href'. ЛИБО можно работать как со словарем, обрабатывать ключ-значение

main()

def main2():  # Парсинг тэгов с главной страницы
  base = 'https://ru.stackoverflow.com'
  html = requests.get(base).content
  soup = BeautifulSoup(html, 'lxml')
  div = soup.find('div', id = 'recent-tags-list')
  a = div.find_all('a', class_ = 'post-tag')


  for _ in a:
    print(_.getText())  # Взятие текста методом getText

main2()