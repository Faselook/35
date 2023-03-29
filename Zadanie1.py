class Human():
    counter = 0

    def __init__(self,name):
        Human.counter = self.counter + 1
        self.__name = name

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getCiunter(self):
        return Human.counter

    def out(self):
        print("Human = ", self.__name)
    

class Builder(Human):
    counter = 0

    def __init__(self, name, prof):
        super().__init__(name)
        self.__prof = prof

    def getProf(self):
        return self.__prof
    
    def setProf(self, prof):
        self.__prof = prof

    def getCiunter(self):
        return Builder.counter

    def out(self):
        print("Builder = ", self.__prof)
     

class Sailor(Human):
    counter = 0

    def __init__(self, name, prof):
        super().__init__(name)
        self.__prof = prof

    def getProf(self):
        return self.__prof
    
    def setProf(self, prof):
        self.__prof = prof

    def getCiunter(self):
        return Sailor.counter

    def out(self):
        print("Sailor = ", self.__prof)


class Pilot(Human):
    counter = 0

    def __init__(self, name, reis):
        super().__init__(name)
        self.__reis = reis

    def getReis(self):
        return self.__reis
    
    def setReis(self, reis):
        self.__reis = reis

    def getCiunter(self):
        return Pilot.counter

    def out(self):
        print("Pilot = ",self.__reis)

list = [Human("User"), Builder("builder", "welder"), Sailor("sailor", "cap"), Pilot("pilot", 100)]

def out(list):
    for el in list:
        el.out()

out(list)

print("-------------------------------------------")
def getCounter(list):
    for el in list:
        print(el.getCounter())

out(getCounter)