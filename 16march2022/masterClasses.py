class Classz:
    """This is a Help Text to understand why is this even
    anyways don't worry its just is
    no can do shitt"""
    def __init__(self, first_name, middle_name, last_name, dobirth):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dobirth = dobirth
        #This following will print the following statement without calling any method.
        print("The user name is " + self.first_name + " " + self.middle_name + " " + self.last_name +
         " and his age is " )
    
    #This method would have to be called by ClassName.method_name() 
    def displayf(self):
        ageis = 40
        print("Method called using .method_name() " + "the name is " 
        + self.first_name + " " + self.middle_name 
        + " " + self.last_name + ", " + str(ageis) + " years.")

user0default = Classz("Ram", "Ajore", "Pal", 19711223)
user0default.displayf()


class Classx:
    print()

user1default = Classx()

user1default.first_name = "Ram"
user1default.middle_name = "Kumar"
user1default.last_name = "Sharma"



""" user1input = Classx()

user1input.first_name = input("Please Enter your first name : ")
user1input.middle_name = input("Please Enter your middle name : ")
user1input.last_name = input("Please Enter your last name : ") """


#CLASS with inherritance

class A(object):
    def __init__(self, something):
        print("A init called into ")
        self.something = something

class B(A):
    def __init__(self, something):
        super().__init__(something)