days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']
breakfast = ['Bread', 'Egg', 'Oat', 'Junk', 'Junk1', 'Junk2', 'Junk3' ]
lunch =  ['Rice', 'Yam', 'Semo'] 
dinner = ['Fish stew', 'Beans', 'Pepperoni']

diet = []

for day in days_of_week:
    for fast in breakfast:
        diet.append(day)
        diet.append(fast)

print(diet)

# diet= [[day,meal for day,meal in days_of_week, breakfast] for i in range(0,7)]
# print(diet)



# Day         breakfast    lunch       dinner
# sunday  - 
# monday
# tuesday
# wednesday
# thursday
# friday
# saturday