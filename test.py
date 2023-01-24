# newlist = []
# row = 7
# col = 4
# for x in range (0, row): 
#   newlist.append([])

#   for y in range(0, col):
#     newlist[x].append('R' + str(x) + 'C' + str(y))

# print(newlist)

diet = []
days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
breakfast = ['Bread', 'Egg', 'Oat', 'Junk', 'Junk1', 'Junk2', 'Junk3' ]
lunch =  ['Rice', 'Yam', 'Semo'] 
dinner = ['Fish stew', 'Beans', 'Pepperoni']


for day,fast,lun,dine in zip(days_of_week,breakfast,lunch,dinner):
    diet.append([day,fast,lun,dine])

print(diet)