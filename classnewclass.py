class Car:
    def __repr__(self):
        return "Car()"
    #def __str__(self):
    #    return "member of Car"

TataNexon = Car()
TataNexon.price = 14000
TataNexon.owner = "Prashant"
TataNexon.city = "Bengaluru"
TataNexon.buydate = "April 2022"

print(TataNexon)