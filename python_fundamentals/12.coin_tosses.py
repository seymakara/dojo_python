import random
def coinTosses():
    print "Starting the program..."
    headcount=0
    tailcount=0
    for i in range(5):
        res = random.randint(0, 1)
        if res == 0:
            headcount += 1
            print "Attempt #", i, ": Throwing a coin... It's a head! ... Got ", headcount, "head(s) so far and ", tailcount, " tail(s) so far"
        else:
            tailcount += 1
            print "Attempt #", i, ": Throwing a coin... It's a tail! ... Got ", tailcount, "head(s) so far and ", headcount, " head(s) so far"
    
    print "Ending the program, thank you!"

coinTosses()
