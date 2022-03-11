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

""" 2What is the purpose of the pass statement in Python?

a.It is used to skip the yield statement of a generator and return a value of None.
b.It is used to pass control from one statement block to another.
c.It is a null operation used mainly as a placeholder in functions, classes, etc. <----
d.It is used to skip the rest of a while or for loop and return to the start of the loop. """
