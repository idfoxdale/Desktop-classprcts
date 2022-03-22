#https://www.w3schools.com/python/python_inheritance.asp

from re import S

from attr import s


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student1(Person):
  pass

x1 = Student1("Mike", "Olsen")
x1.printname()

class Student(Person):
  def __init__(self, fname, lname):
      #The child's __init__() function overrides the inheritance of the parent's __init__() function.
      Person.__init__(self, fname, lname)
      #To keep the inheritance of the parent's __init__() function, 
      # add a call to the parent's __init__() function


class StudentS(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    #By using the super() function, you do not have to use the name of the parent element, 
    # it will automatically inherit the methods and properties from its parent.



class Animal:
    def __init__(self, animalname, kidname, voice, waterornot):
        self.aname = animalname
        self.kname = kidname
        self.vce = voice
        self.won = waterornot

    def printani(self):
        print("%s is an animal, it has kid %s, %s likes to make sound known as %s, %s they like to live in water ") 
                 


txt = "The best things in life are free!"
print("expensive" not in txt)