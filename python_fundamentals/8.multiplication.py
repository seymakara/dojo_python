numbers = ['x',1,2,3,4,5,6,7,8,9,10,11,12]

for i in range(0, len(numbers)): # i for the numbers below x
    row = " "
    if i == 0:
        row += "x "
        for j in range(1, len(numbers)): #j is for the items other than x in the first colum
            row += str(numbers[j]) + " "
    else:
        row += str(i) + " "
        for j in range(1, len(numbers)):
            row += str(numbers[i]*numbers[j]) + " "
    print row