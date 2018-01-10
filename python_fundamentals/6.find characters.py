word_list = ['hello','world','my','name','is','Anna']
char = 'm'
new_list = []
def findCharacters(x,y):
    for i in x:
        if y in i:
            new_list.append(i)
    print new_list
findCharacters(word_list, char)

