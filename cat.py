from pet_constructor import Cat

cat1 = Cat(2, 'мальчик', 'Барон')
cat2 = Cat(2, 'мальчик', 'Сэм')

print(cat1.get_a())  # Вызов метода get_a класса Cat
print(cat2.get_a())

print(vars(cat1))  # возвращает все атрибуты объекта в виде словаря
