class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price >10000:
            self.tax = "{}%".format(15)
        else:
            self.tax = "{}%".format(12)
        self.display_all()

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}mph".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}mpg".format(self.mileage)
        print "Tax: {}".format(self.tax)
        print " "

car1 = Car(15000, 120, "Full", 40)
car2 = Car(600, 100, "Empty", 20)
car3 = Car(3300, 110, "Full", 30)
car4 = Car(8800, 110, "Full", 25)
car5 = Car(24300, 130, "Empty", 50)
car6 = Car(35000, 130, "Kind of Full", 55)