count = int(input('Участников конференции: '))
price = 0
for i in range(count):
    age = int(input(f'Введите возраст участника {i}: ')) # TODO Вставить счётчик, i не работает?
    if 18 <= age <= 24:
        price += 990
    elif age > 24:
        price += 1390
if 3 <= count:
    price = price * 0.9
print (round(price))
