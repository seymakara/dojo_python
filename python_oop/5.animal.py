class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        if self.health <= 0:
            print "RIP :("
        else:
            print "{} has {} health left".format(self.name, self.health)
        return self

Animal1= Animal("cat", 9)
Animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name): #calls animal init. should write all the required parameters
        super(Dog, self).__init__(name, 150) #overriding default health which is 100
   
    def pet(self):
        self.health += 5
        return self

Animal2= Dog("Musfik")
Animal2.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    
    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        super(Dragon, self).display_health() #callin super's display_health function in order to modify it (added i am a dragon part). Def Names should be same
        print "I am a Dragon"

Animal3 = Dragon("Smaug")
Animal3.run().run().run().fly().fly().fly().fly().display_health()

