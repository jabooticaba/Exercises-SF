class Cat:
    def __init__(self, age = '', gender = '', name = ''):
        self.age = age
        self.gender = gender
        self.name = name
        
    def __str__(self):
        return f"Name: {self.name} \nSex: {self.gender} \nAge: {self.age}"
#        return "Имя: {0} \nпол: {1} \nвозраст: {2}".format(self.name, self.gender, self.age)
#        return self.name, self.gender, self.age        
