def multiply(list,x):
    newlist = []
    for i in list:
        i*=x
        newlist.append(i)
    return newlist
a = [2,4,10,16]
multiply(a,5)

def odd_even():
    for i in range (1,50):
        if i%2==0:
            print "Number is", i, "This is an even number."
        else:
            print "Number is", i, "This is an odd number."
odd_even()

def layered_multiples(list):
    newList = []
    for i in list: #for a nested list 
        nestList =[] 
        for j in range(0,i): # loops through as many as the item in the list
            nestList.append(1) #prints that many 1s in a list
        newList.append(nestList) # adds lists of ones in a new list
    return newList

x = layered_multiples(multiply([2,4,5],3))
print x
    
