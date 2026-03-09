#OOPS
#Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

car1 = Car()
car1.start()

#Encapsulation
class Car:
    
    def start(self):
        self.__fuel_system()
        self.__engine_start()
        print("Car started")

    def __fuel_system(self):
        print("Fuel system activated")

    def __engine_start(self):
        print("Engine started")


c = Car()
c.start()