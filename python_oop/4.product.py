class Product(object):
    def __init__(self, price, name, weight, brand, status = "For Sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "Sold!"
        return self

    def addTax(self):
        self.price += self.price * .08
        return self.price

    def returning(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        if reason == "in the box, like new":
            self.status = "For Sale"
        if reason == "box opened":
            self.status = "Used"
            self.price -= self.price * .2
        return self

    def displayinfo(self):
        print "Name: {}".format(self.name)
        print "Brand: {}".format(self.brand)
        print "Price: {}$".format(self.price)
        print "Weight: {}lbs".format(self.weight)
        print "Status: {}".format(self.status)
        print "--------"
        print " "
        return self
        
        
Product1 = Product(1650, "Phone", 0.5, "Samsung")
Product1.addTax() # no dosplay info because it returns price not self.So display info is right before the .sell
Product1.displayinfo().sell().displayinfo()
Product1.returning("box opened").displayinfo()




