# prints all odd numbers from 1 to 1000
for i in range (1, 1000): #loops through the numbers till 1000
    if i%2 == 1: #checks if the modulo is 1
        print i #prints the number

#prints multiples of 5 from 5 to 1M
for i in range (5, 1000000): #loops through the numbers till 5000
    if i%5 == 0: #checks if the modulo is 0
        print i #prints the number

#sums all the values in a list.
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range (len(a)):
    sum+=a[i]
print sum

#prints the average of the values in the list.
a = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0
for i in range (len(a)):
    sum+=a[i]
avg = sum/ len(a)
print avg
