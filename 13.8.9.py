count = int(input('Участников конференции: '))
price = 0
for i in range(count):
    age = int(input('Введите возраст участника: ')) # TODO Вставить счётчик
    if 18 <= age <= 24:
        price += 990
    elif age > 24:
        price += 1390
if count >= 3:
    price = price * 0.9
print (round(price))
