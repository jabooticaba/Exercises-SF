'''
ЗАДАНИЕ:
Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге,
читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов,
и наиболее длинное слово на английском языке.

В файле ожидается смешанный текст на двух языках — русском и английском.
'''

fileName = input('Введите имя файла:')

myFile = open(fileName, 'r')  # TODO раскомментить ввод имени файла и вставить переменную

workString = (myFile.read().lower())  # Приведение к одному регистру


def char_replacer(string):  # Функция убирает указанные символы из строки
    for ch in ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', ',']:
        if ch in string:
            string = string.replace(ch, "")
    return string

rawList = char_replacer(workString).split()

# Цикл находит элементы списка с англ. символами, считает символы и выводит элемент с наибольшим количеством
eng_alpha = 'abcdefghijklmnopqrstuvwxyz'
lenght = 0
for i in rawList:
    for x in i:
        if x in eng_alpha:
            if len(i) > lenght:
                lenght = len(i)
                list_max_word = i

print(list_max_word)

# Цикл составляет словарь из слов длиной более 3 символов
dict = {}
for i in rawList:
    if i not in dict and len(i) > 3:
        dict[i] = 1
    elif i in dict and len(i) > 3:
        dict[i] += 1

print(list(dict.keys())[list(dict.values()).index(max(dict.values()))])  # Вывод ключа словаря с наибольшим значением
# print(dict.get(list(dict.keys())[list(dict.values()).index(max(dict.values()))]))  # Опционально количество вхлождений самого популярного слова

