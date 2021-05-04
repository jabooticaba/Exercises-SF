# 16.9.1
class Triangle:
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.__class__.__name__} \nДлина стороны а: {self.a}, \nДлина стороны b: {self.b}, \nДлина стороны c:' \
               f' {self.c}, \nКоординаты: x {self.x}, y {self.y}, \nПлощадь: {self.get_area()}'

    def get_area(self):
        p = ((self.a + self.b + self.c)/2)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


tri = Triangle(3, 3, 3, 0, 0)
print(tri)


# 16.9.2

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

rect = Rectangle(5,10)

print(rect.get_area())

# 16.9.3

class Client:
    className = "Клиент"
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        return f'{self.className} "{self.name}". Баланс: {self.balance} руб'

client1 = Client("Иван Петров", 50)

print(client1.display())


# 16.9.4

def id_generator():
    for i in range(1, 10001):
        yield i


gen = id_generator()


class Employee:
    def __init__(self, name, id =''):
        self.name = name
        self.id = id


class Volunteer(Employee):
    def __init__(self, name, city, status):
        self.city = city
        self.status = status
        Employee.__init__(self, name, "E" + str(next(gen)))

    def display(self):
        return f'{self.name}, г.{self.city}, статус "{self.status}"'


vol = Volunteer("Иван Петров", "Москва", "Наставник")

print(vol.display())
