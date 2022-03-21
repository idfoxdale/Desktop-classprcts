class Parent1:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        print("Current instance parameters are parameter#1 = " + str(param1) + ", and parameter#2 = " + str(param2))

objty1 = Parent1("Ram", "Ramayan")
objty2 = Parent1("Krishna", "Geeta")

class Childz1(Parent1):
    pass

chilobj1 = Childz1("Luv", "Kush")

print('The value of pi is: %5.4f' %(3.141592))
print('{2} {1} {0}'.format('directions', 'the', 'Read'))

##new class style guide

class Employee:
    id = 10
    name = "John Snow"

    def display(self):
        print("Employee ID: %d \nName: %s"%(self.id, self.name))

#Creating a emp instance of Employee class

emp = Employee()
emp.display()
