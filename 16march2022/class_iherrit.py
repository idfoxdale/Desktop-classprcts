class Basee:
    def __init__(self):
        print("Base Created") 

class Child1(Basee):
    def __init__(self):
        Basee.__init__(self)

class Child2(Basee):
    def __init__(self):
        super(Child2, self).__init__()


Child1()

Child2()