class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price =  price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayInfo(self):
        print "Price:", self.price, "$", "Max Speed:", self.max_speed, "mph", "Miles:", self.miles
        return self
    def ride(self):
        print "Riding..."
        self.miles+=10
        return self
    def reverse(self):
        print "Reversing..."
        if self.miles >= 5:
            self.miles -= 5
        if self.miles-5 < 0:
            self.miles = 0
        return self

bike1 = Bike(500, 25, 100)
bike2 = Bike(1200, 30, 60)
bike3 = Bike(10000, 30, 0)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()