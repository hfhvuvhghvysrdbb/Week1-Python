#Quiz

name = "natsirT"
print(name)

favouriteNumber = 7

for i in range (1, favouriteNumber**2 + 1):
    print(i)

class Engineers:
    def __init__(self, name, type, yearsOfExperience):
        self.skill = "problem solver"
        self.name = name
        self.type = type
        self.yearsOfExperience = yearsOfExperience

e1 = Engineers("James", "Mechanical", 3)
e2 = Engineers("Sarah", "Electronics", 2)

print(e1.__dict__)
print(e2.__dict__)