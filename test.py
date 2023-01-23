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

for x in range(0,7):
    diet.append([])

    for day in days_of_week:
        diet[x].append(day)

print(diet)