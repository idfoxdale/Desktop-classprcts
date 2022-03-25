from itertools import count


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
