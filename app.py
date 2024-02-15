class Person:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
        print("Hi vijay")

    def details(self):
        print("Person name  :", self.name)
        print("Person age  :", self.age)

    def education(self):
        print("He has comleted in ", self.year)
