count = int(input('Участников конференции: '))
price = 0
for i in range(count):
    print('Введите возраст участника #', i + 1, ': ', sep ='', end='') # формат строки ввода возраста участников
    age = int(input())
    if 18 <= age <= 24:
        price += 990
    elif age > 24:
        price += 1390
if 3 <= count:
    price = price * 0.9
print (round(price))
