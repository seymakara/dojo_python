users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printnames(users):
    for person in users:
        print person
        count = 0
        for i in users[person]:
            count+=1
            print count, "-", i['first_name'], i['last_name'],"-", len(i['first_name'])+len(i['last_name'])
printnames(users)
