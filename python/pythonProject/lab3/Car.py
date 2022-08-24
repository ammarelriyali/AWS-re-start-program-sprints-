
class Car:
    def __init__(self,name,fuelRate = 100,velocity=60):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity
    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, i):
        try:
            if i > 100 or i<0:
                self.__velocity = 100
            else:
                self.__velocity= i
        except:
            print("invald input")
    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, i):
        try:
            if i > 100 or i<0:
                self.__fuelRate = 100
            else:
                self.__fuelRate = i
        except:
            print("invald input")

    def run(self, distance, velocity):
        try:
            self.velocity = velocity
            while True:
                if distance > 0:
                    distance = distance - 10
                    self.__fuelRate -= (self.__fuelRate * .10)
                    if self.__fuelRate <= 0.9:
                        Car.stop(self)
                        break
                else:
                    break
        except:
            print("invald input")

    def stop(self):
        self.__velocity=0
        print("you arrive the destination")

# c=Car("fat",10)
# c.run(100,100)
# print(c.fuelRate)