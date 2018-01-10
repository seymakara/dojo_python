class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, *num):
        for i in num:
            if type(i) == tuple:
                for j in i:
                    self.value += j
                print "valuetuple=", self.value
            elif type(i) == list:
                for j in i:
                    self.value += j
                print "valuelist=", self.value
            else:
                self.value += i
                print "valuesingle=", self.value
        return self

    def subtract(self, *num):
        for i in num:
            if type(i) == tuple:
                for j in i:
                    self.value -= j
                print "valuetuple=", self.value
            elif type(i) == list:
                for j in i:
                    self.value -= j
                print "valuelist=", self.value
            else:
                self.value -= i
                print "valuesingle=", self.value
        return self

md= MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3])
print "final value", md.value