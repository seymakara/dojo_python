my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makingtuples(dict):
  newList = []
  for key in dict:
    newList.append((key, dict[key]))
  return newList

print makingtuples(my_dict)

# #solution2
# def making_tupes(the_dict):
#     the_list = []
#     # here, k and v will parse each tuple of key,value pairs returned by .iteritems()
#     for k, v in the_dict.iteritems():
#         the_list.append((k,v))
#     return the_list
