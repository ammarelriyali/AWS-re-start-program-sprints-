import Person
from re import match



class Employee(Person.Person):
    id=0
    def __init__(self, name, car, email, distanceToWork, salary=1000):
        super(Employee, self).__init__(name)
        self.car = car
        self.email = email
        self.distanceToWork = distanceToWork
        self.salary = salary
        self.id+=1
        Employee.increse()

    @classmethod
    def increse(cls):
        cls.id+=1
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, i):
        if i > 999:
            self.__salary = i
        else:
            self.__salary = 1000

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, e):
        pat = r"^([a-z]|[0-9]|\-|\_|\+|\.)+\@([a-z]|[0-9]){2,}\.[a-z]{2,}(\.[a-z]{2,})?$"
        if match(pat, e):
            self.__email = e
        else:
            self.__email = "none"

    def send_mail(self):
        pass

    def refuel(self, gasAmount):
        self.car.fuelRate = gasAmount

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def work(self, hours):
        try:
            if hours >= 24 or hours <= 0:
                print("error invald housrs")
            elif hours == 8:
                self.mood = Person.Person.moods[0]
            elif hours < 8:
                self.mood = Person.Person.moods[1]
            else:
                self.mood = Person.Person.moods[2]
        except:
            print("error pls enter number olny")


