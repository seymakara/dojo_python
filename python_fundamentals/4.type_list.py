x = ['magical unicorns',19,'hello',98.98,'world']
y = [2,3,1,7,4,12]
z = ['magical','unicorns']
def typeList(arr):
    sum = 0
    string_list = []
    for i in range(len(arr)): 
        if isinstance(arr, int) or isinstance(arr, float):
            sum+=arr[i] #sums items in the list if they are numbers
        elif type(arr[i]) == str:
            string_list.append(arr[i]) #concatenates item onto a new string if they are string
            
    if sum != 0:
        print "Sum:", sum #prints sum if it is not empty
    if len(string_list) != 0: #prints new string if it is not empty
        print ' '.join(string_list)
    
    if sum > 0 and len(string_list) > 0: #checks for the presence of number and string for mixed type
        print "The list you entered is of mixed type"
    elif len(string_list) > 0:
        print "The list you entered is of string type" #checks for the presence of string for string type
    elif sum > 0:
        print "The list you entered is of integer type" #checks for the presence of number for integer type
typeList(x)
    




