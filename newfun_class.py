class Employee:
    id = 10
    name = "Ajay"

    def display(self):
        print(self.id, self.name)
        print("ID: %d \nName: %s"%(self.id,self.name))

emp = Employee()
emp.display()
