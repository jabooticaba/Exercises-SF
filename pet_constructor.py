class Cat:
    def __init__(self, age = '', gender = '', name = ''):
        self.age = age
        self.gender = gender
        self.name = name
        
    def print_(self):
        print(f'Имя: {self.name} \nпол: {self.gender} \nвозраст: {self.age}')
        
