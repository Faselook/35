class User():

    countUser = 0

    def __init__(self, firstName, age):
        User.countUser = self.countUser + 1
        self.__firstName = firstName
        self.__age = age

    def getCU(self):
        return self.countUser
    
u = User("User1", 39)
u2 = User("User2", 84)
print(u.getCU())
print(u2.getCU())