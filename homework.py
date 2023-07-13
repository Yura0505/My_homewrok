class strDescriptor:
    def __set_name__(self, obj, name):
        self.name = "_" + name
        setattr(obj, self.name, None)

    def __init__(self, minLen):
        self.minLen = minLen

    def __get__(self, obj, objtype):
        value = getattr(obj, self.name)
        return value

    def __set__(self, obj, value):
        if not isinstance(value, str):
            print("Значення не є рядком!")

        elif len(value) == 0:
            print("Значення не можу бути порожнім!")

        elif len(value) <= self.minLen:
            print(f"Значення закоротке! Повино бути більше {self.minLen} символів!")

        else:
            setattr(obj, self.name, value)


class numDescriptor:
    def __set_name__(self, obj, number):
        self.number = "_" + number
        setattr(obj, self.number, None)

    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def __get__(self, obj, objtype):
        value = getattr(obj, self.number)
        return value

    def __set__(self, obj, value):
        if self.minValue > value or self.maxValue < value:
            print(f"Значення повино бути в діапазоні від {self.minValue} до {self.maxValue}!")

        else:
            setattr(obj, self.number, value)


class User:
    firstname = strDescriptor(3)
    lastname = strDescriptor(4)
    age = numDescriptor(18, 60)
    followers = numDescriptor(0, 999)

    def __init__(self, firstname, lastname, age, followers):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.followers = followers

    def showInfo(self):
        print(f"First name: {self.firstname}\n"
              f"Second name: {self.lastname}\n"
              f"Age: {self.age}\n"
              f"Follow: {self.followers}\n")


user1 = User("Bryan", "McDale", 50, 150)
user2 = User("Yura", "Kryvyi", 20, 550)

user1.showInfo()

user1.firstname = "Nate"
user1.lastname = "Es"
user1.age = 60
user1.followers = 9999

user1.showInfo()
user2.showInfo()
