class myClassNewq:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method_classFunct(self):
        print("The method class function output is " + self.param1 + self.param2)


#now calling function 

object1 = myClassNewq("Ram, ", "Sita")

object1.method_classFunct()


class childClass(myClassNewq):
    pass

childobjct1 = childClass("Luv, ", "Kush")
childobjct1.method_classFunct()


