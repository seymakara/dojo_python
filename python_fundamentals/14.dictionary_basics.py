me = {
    "name" : "Seyma",
    "age" : "29",
    "country": "Turkey",
    "language": "Python"
}

def printme(x):
    print "My name is {}".format(me["name"])
    print "My age is {}".format(me["age"])
    print "My country of birth is {}".format(me["country"])
    print "My favorite language is {}".format(me["language"])
printme(me)