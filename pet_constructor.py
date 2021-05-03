class Cat:
    def __init__(self, age = '', gender = '', name = ''):
        self.age = age
        self.gender = gender
        self.name = name
        
    def get_a(self):
        return "Имя: {0} \nпол: {1} \nвозраст: {2}".format(self.name, self.gender, self.age)
        
