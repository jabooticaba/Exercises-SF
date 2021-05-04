# 16.9.1

class Triangle:
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.__class__.__name__} \nДлина стороны а: {self.a}, \nДлина стороны b: {self.b}, \nДлина стороны ' \
               f'c:' \
               f' {self.c}, ' \
               f'\nКоординаты: x {self.x},' \
               f' y {self.y}, \nПлощадь: {self.get_area()}'

    def get_area(self):
        p = ((self.a + self.b + self.c)/2)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


tri = Triangle(3, 3, 3, 0, 0)
print(tri)


# 16.9.2
