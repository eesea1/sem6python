class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def turnon(self):
        print("Автомобиль заведен!")

    def turnoff(self):
        print("Автомобиль заглушен")

    def setColor(self, ncolor):
        self.color = ncolor

    def setType(self, ntype):
        self.type = ntype

    def setYear(self, nyear):
        self.year = nyear