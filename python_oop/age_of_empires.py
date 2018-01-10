
class Human(object):
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    def takeDmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            print "Oh god I'm dead!"

class Archer(Human):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 10

class Building(object):
    def __init__(self, x, y, hp, image, cap):
        self.x = x
        self.y = y
        self.hp = hp
        self.image = image
        self.cap = cap

    def burn(self):
        self.hp -= 10
        return self

class MilitaryBuilding(Building):
    def __init__(self, x, y, image, dmg = 10):
        super(MilitaryBuilding, self).__init__(x, y, 150, image, 10)
        self.dmg = dmg

    def shoot(self, human):
        human.takeDmg(self.dmg)

class Stable(MilitaryBuilding):
    def __init__(self, x, y):
        super(Stable, self).__init__(x, y, "stable.png", 50)
        self.hp = 200

asdf = Building(10,25,100, "default.png", 5)
asdf.burn().burn().burn()

print type(asdf)

something = MilitaryBuilding(5,90, "military.png")
something.burn()

print isinstance(something, int)

stable = Stable(2345,543)
stable.burn()

print stable.hp
print isinstance(stable, Stable)
print isinstance(stable, MilitaryBuilding)
print isinstance(stable, Building)

guywhogetsshot = Archer(34,34)
archer = Archer(34,34)

stable.shoot(guywhogetsshot)

print archer.hp

