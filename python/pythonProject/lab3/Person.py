class Person:
    moods=("happy","lazy","tired")
    def __init__(self, name, money=1000, mood="happy", healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, i):
        if i > -1 and i<101:
            self.__healthRate= i
        else:
            self.__healthRate = 100

    def sleep(self, hours):
        try:
            if hours >= 24 or  hours <= 0:
                print("error invald housrs")
            elif hours == 7:
                self.mood = Person.moods[0]
            elif hours > 7:
                self.mood = Person.moods[1]
            else:
                self.mood = Person.moods[2]
        except:
            print("error pls enter number olny")


    def eat(self, meals):
        try:
            if meals == 3:
                self.healthRate = 100
            elif meals == 2:
                self.healthRate = 75
            elif meals==1:
                self.healthRate = 50
            else :
                print("enter number between 1 and 3")
        except:
            print("error pls enter number only")


    def buy(self,item):
        try :
            self.money=self.money-(item *10)
        except:
            print("error pls enter number olny")


