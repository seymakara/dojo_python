words = "It's thanksgiving day. It's my birthday,too!"
print "position of day:", words.find("day")
print "new words:", words.replace("day", "month")

x = [2,54,-2,7,12,98]
def minmax(x):
    print "min", min(x)
    print "max", max(x)
minmax(x)

x = ["hello",2,54,-2,7,12,98,"world"]
def firstlast(x):
    print "first", x[0]
    print "last", x[len(x)-1]
firstlast(x)

x = [19,2,54,-2,7,12,98,32,10,-3,6]
def newlist(x):
    sorted = x.sort()
    half = len(x)/2
    firsthalf= x[:half] 
    print firsthalf
    lasthalf= x[half:]
    print lasthalf
    lasthalf.insert(0, firsthalf)
    print lasthalf
newlist(x)