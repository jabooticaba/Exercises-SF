count = int(input('Участников конференции:'))
price = 0
for i in range(count):
    print(f'Введите возраст участника #{i + 1}: ', end='')
    age = int(input())
    if 18 <= age <= 24:
        price += 990
    elif age > 24:
        price += 1390
if count >= 3:
    price = price * 0.9
print(f'Сумма к оплате: {round(price)}')
