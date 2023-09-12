from Student import Student
from Math import Math
from Car import Car


class P12:
    def __init__(self):
        pass

    @staticmethod
    def prak12(self):
        i = Student("Evgenii", 19, "PI3-1b")
        a = Student("Vasya", 20, "kredit")
        b = Student("eze", 22, "pop")
        c = Student("tyt", 24, "pap")
        d = Student("ret", 18, "sdfafsa")
        print("name = ", i.getName(), "age = ", i.getAge(), "groupNumber = ", i.getGN())
        print("name = ", a.getName(), "age = ", a.getAge(), "groupNumber = ", a.getGN())
        m = Math(10, 5)
        m.div()
        car1 = Car("blue", "hz", "2005")
        car2 = Car("red", "hz", "2003")
        print("color = ", car1.color, "type = ", car1.type, "year = ", car1.year)
        car1.turnon()
        car1.turnoff()
        print("color = ", car2.color, "type = ", car2.type, "year = ", car2.year)