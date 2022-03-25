class Employee:
    id = 10
    name = "Ajay"

    def display(self):
        print(self.id, self.name)
        print("ID: %d \nName: %s"%(self.id,self.name))

emp = Employee()
emp.display()

#deleting the propert of an object

#del emp.id
#del emp

emp.display()


class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1

s1 = Student()
s2 = Student()
s3 = Student()
s4 = Student()
print("Number of student object: ", Student.count)


#python non-parameterised constructor

class Students:
    #Constructor non-parameterised
    def __init__(self):
        print("This is a non parameterized constructor")
    
    def show(self, name):
        print("Hello, ", name)

studentA = Students()
studentA.show("John Snow")

class Employeee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def displaye(self):
        print("The employee ID is %d , their name is %s"%(self.id,self.name))

empee1 = Employeee(786, "Ezra")
empee7 = Employeee(747, "Bond")

mylist1 = []

mytuple1 = ()

mydict1 = {}

myset1 = {"apple", "banana", "cherry"} 
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
setn1 = {"abc", 34, True, 40, "male"}
print("myset1 original - ", myset1)
myset1.add("orange")
print("myset1 original .add(orange) - ", myset1)
myset1.update(set1)
print("myset1.update(set1) - ", myset1)
#Set items are unordered, unchangeable, and do not allow duplicate values.

print(type(mylist1))
print(type(mytuple1))
print(type(mydict1))
print(type(myset1))

bondn = str(7).zfill(3)
print(bondn)