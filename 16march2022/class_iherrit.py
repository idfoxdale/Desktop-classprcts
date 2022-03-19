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

# Python program to
# demonstrate init with
# inheritance

class A(object):
	def __init__(self, something):
		print("A init called")
		self.something = something
		

class B(A):
	def __init__(self, something):
		# Calling init of parent class
		A.__init__(self, something)
		print("B init called")
		self.something = something
		
obj = B("Something")


# Python program to
# demonstrate init with
# inheritance

class A(object):
	def __init__(self, something):
		print("A init called")
		self.something = something
		

class B(A):
	def __init__(self, something):
		print("B init called")
		self.something = something
		# Calling init of parent class
		A.__init__(self, something)
		
obj = B("Something")
