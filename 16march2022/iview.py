from unicodedata import name
for i in [1, 2, 3, 4][::-1]:
    print (i)
# 4
# 3
# 2
# 1

names = ['Chris', 'Jack', 'John', 'Daman']
print("The ouptut is = " + names[-1][-3])

# 'Daman', 'John', 'Jack'

name_set = (set(names))


print(name_set)

print(names)

""" class myClass:
    def __init__(self, attrib1, attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        print("myClass inst " + " " + attrib1 + " " + attrib2)

    def display(self):
        print(self.attrib1, self.attrib2)


objectc1 = myClass("Ram", "Laxman")

objectc1.display()

class childClass(myClass):
    pass

objectcc2 = childClass("Ram Child", "Laxman Child") """


class MyClass:
    pass

object1 = MyClass()
object1.attrib1 = "Attrib1"
object1.attrib2 = "Attrib2"

print(object1)
