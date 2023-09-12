class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGN(self):
        return self.groupNumber

    def setNameAge(self, newname, newage):
        self.name = newname
        self.age = newage

    def setGN(self, newGN):
        self.groupNumber = newGN