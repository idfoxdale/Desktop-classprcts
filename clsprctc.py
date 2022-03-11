class newClass():
    def __init__(self, name, age,):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def __repr__(self):
        return f"{self.name} is {self.age} years old"

mynewlist = [newClass("John", 20), newClass("Jane", 21), newClass("Jack", 22)]

print(mynewlist)
print(mynewlist[0])
print(mynewlist[0].name)
print(mynewlist[0].age)
mynewlist[0].age = 30
print(mynewlist[0].age)
