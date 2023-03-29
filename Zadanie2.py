class Passport():
    def __init__(self, contry, name, age, adress):
        self.__contry = contry
        self.__name = name
        self.__age = age
        self.__adress = adress

    def getContry(self):
        return self.__contry
    
    def setContry(self, contry):
        self.__contry = contry

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age = age

    def getAdress(self):
        return self.__adress
    
    def setAdress(self, adress):
        self.__adress = adress

    def out(self):
        print("Passport = ", self.__contry, self.__name, self.__age, self.__adress)

    country = property(getContry, setContry)
    name = property(getName, setName)
    age = property(getAge, setAge)
    adress = property(getAdress, setAdress)

class ForeignPassport(Passport):

    def __init__(self, contry, name, age, adress, visa, numberPassport):
        super().__init__(contry, name, age, adress)
        self.__visa = visa
        self.__numberPassport = numberPassport
    
    def getVisa(self):
        return self.__visa
    
    def setVisa(self, visa):
        self.__visa = visa

    def getNumberPassport(self):
        return self.__numberPassport
    
    def setNumberPassport(self, numberPassport):
        self.__numberPassport = numberPassport

    def out(self):
        print("ForeignPassport = ",self.__visa, self.__numberPassport, self.__contry, self.__name, self.__age, self.__adress)

    visa = property(getVisa, setVisa)
    numberPassport = property(getNumberPassport, setNumberPassport)



list = [Passport()]

def out(list):
    for el in list:
        el.out()

out(list)