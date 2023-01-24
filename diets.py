days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']

#Underweight diet
under_diet = []
breakfast = ['Bread', 'Egg', 'Oat', 'Junk', 'Junk1', 'Junk2', 'Junk3' ]
lunch =  ['Rice', 'Yam', 'Semo'] 
dinner = ['Fish stew', 'Beans', 'Pepperoni']

#Normal diet
under_diet = []
breakfast = ['Bread', 'Egg', 'Oat', 'Junk', 'Junk1', 'Junk2', 'Junk3' ]
lunch =  ['Rice', 'Yam', 'Semo'] 
dinner = ['Fish stew', 'Beans', 'Pepperoni']

#Overweight diet
under_diet = []
breakfast = ['Bread', 'Egg', 'Oat', 'Junk', 'Junk1', 'Junk2', 'Junk3' ]
lunch =  ['Rice', 'Yam', 'Semo'] 
dinner = ['Fish stew', 'Beans', 'Pepperoni']

#Obese diet
under_diet = []
breakfast = ['Bread', 'Egg', 'Oat', 'Junk', 'Junk1', 'Junk2', 'Junk3' ]
lunch =  ['Rice', 'Yam', 'Semo'] 
dinner = ['Fish stew', 'Beans', 'Pepperoni']

for day,fast,lun,dine in zip(days_of_week,breakfast,lunch,dinner):
    diet.append([day,fast,lun,dine])

print(diet)

