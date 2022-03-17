from unicodedata import name


for i in [1, 2, 3, 4][::-1]:
    print (i)

# [4]
# [3]
# [2]
# [1]

names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-3])

# 'Daman', 'John', 'Jack'

type(set(names))

print(names)

class myClass:
    def __init__(self, attrib1, attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2
        print("myClass inst " + " " + attrib1 + " " + attrib2)


objectc1 = myClass("Ram", "Laxman")

class childClass(myClass):
    pass

objectcc2 = childClass("Ram Child", "Laxman Child")
