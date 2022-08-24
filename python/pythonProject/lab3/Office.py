from Employee import Employee
from Car import Car
import datetime as dt


class Office:
    employeesNum = 0

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
    @classmethod
    def change_emps_num(cls,num):
        cls.employeesNum=num

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        try:
            takeTime = (distance * 1000) / velocity
            if takeTime > 1400:
                print("late")
            else:
                x = str(dt.timedelta(minutes=int(takeTime)))
                t1 = dt.datetime.strptime(x, '%H:%M:%S')
                t2 = dt.datetime.strptime(moveHour, '%H:%M:%S')
                time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
                a, b, c = (str((t1 - time_zero + t2).time()).split(":"))
                q,w,r=targetHour.split(":")
                if int(a) < int(q) or (int(a) == int(q) and int(b) == int(w)):
                    print("not late")
                else:
                    print("late")
        except:
            print("invald input")


    def get_all_employees(self):
        return self.employees


    def get_employee(self, id):
        try:
            for i in self.get_all_employees():
                if id == i.id:
                    return i
        except:
            print("invald input")


    def hire(self, e):
        try:
            self.employees.append(e)
        except:
            print("hire method")


    def fire(self, id):
        try:
            for i in self.get_all_employees():
                if id == i.id:
                    self.employees.remove(i)
        except:
            print("invald input")


    def calculate_lateness(self):
        pass


    def check_lateness(self, id, moveHour):
        try:
            for i in self.get_all_employees():
                if id == i.id:
                    takeTime = (i.distanceToWork * 1000) / i.car.velocity
                    if takeTime > 1400:
                        self.deduct(id, 10)
                        break
                    x = str(dt.timedelta(minutes=int(takeTime)))
                    t1 = dt.datetime.strptime(x, '%H:%M:%S')
                    t2 = dt.datetime.strptime(moveHour, '%H:%M:%S')
                    time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
                    a, b, c = (str((t1 - time_zero + t2).time()).split(":"))
                    if int(a) < 9 or (int(a) == 9 and int(b) == 0):
                        self.reward(id, 10)
                    else:
                        self.deduct(id, 10)
                    break

        except:
            print("invald format time")




    def deduct(self, id, deduction):
        try:
            for i in self.get_all_employees():
                if id == i.id:
                    i.salary = i.salary - deduction
        except:
            print("invald input")


    def reward(self, id, reward):
        try:
            for i in self.get_all_employees():
                if id == i.id:
                    i.salary = i.salary + reward
        except:
            print("invald input")


e = Car("fati", 100, 99)
e2 = Car("fati", 100, 120)
e3 = Car("szuz", 80, 160)
e4 = Car("BMW", 90, 110)

c = Employee("amar", e, "amar@gamil.com", 3, 2000)
c1 = Employee("amarmeroo", e2, "amar@gamil.com", 30)
c2 = Employee("amar12", e, "amar@gamil.com", 30)
c3 = Employee("amar13", e3, "amar@gamil.com", 30)
c4 = Employee("amar14", e4, "amar@gamil.com", 30)
f = Office("iti", [c, c1, c2, c3])

f.check_lateness(1, '08:31:00')
print(c.salary)
