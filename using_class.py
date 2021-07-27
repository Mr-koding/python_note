# creating a class

class Vehicle:
    def __init__(self,wheelL,wheelR,Engine,Horsepower):
        self.LeftWheel = wheelL
        self.RightWheel = wheelR
        self.Engine = Engine
        self.HorseP = Horsepower

    def move(self, HP):
        self.Engine += 1
        self.HorseP = HP * self.Engine
        return self.HorseP * 2

    def stop(self):
        self.LeftWheel = 0
        self.RightWheel = 0
        self.Engine = 0
        self.HorseP = 0


aboboya = Vehicle(30,30,150,1000)
bycicle = Vehicle(32,52,533,1990)

aboboya.LeftWheel = 50     

print(aboboya.move(100))
aboboya.stop()
print(aboboya.LeftWheel)

class Car(Vehicle):
    # pass
    
    def __init__(self, bonnet, windscreen):
        self.Bonnet = bonnet
        self.Windscreen = windscreen
        
    
    # def __init__(self, wheelL, wheelR, Engine, Horsepower):
    #     super().__init__(wheelL, wheelR, Engine, Horsepower)

#instantiating an object called Toyota_car from the class Car
Toyota_car = Car("flat",45.5)
Toyota_car.LeftWheel = 30
Toyota_car.RightWheel = 40

# Toyota_car.move(45)
Toyota_car.push = 34

print(Toyota_car.push)


class Motorbike(Vehicle):
    def __init__(self,wheelL,wheelR,Engine,Horsepower):
        super().__init__(wheelL,wheelR,Engine,Horsepower)

jungle_bike = Motorbike(34,56,355,3400)

print(jungle_bike.move(20))
        