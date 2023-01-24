import diets
'''This is a diet-planner that builds ann ideal weekly diet plan based on your weight class for Nigerians.'''

# Collect height and weight to calculate the BMI, returns an error if digits are not entered.
while True:
    try:
        height = float(input("Enter height(cm):"))
        weight = float(input("Enter weight(kg):"))
    except ValueError:
        print("Enter a digit e.g 100")
    else:
        bmi = weight/(0.01*height)**2

    if bmi < 18.5:
        print(f"\nYour bmi is {bmi:.2f}\nYou are underweight dear\n")
        response = input("Would you like a diet to help gain weight:y/n\n")
        if response == 'y':
            print('List of food to eat through the week')
            break
        else:
            print("Fuck you mehn!!")
            break

    elif (bmi > 18.5) and (bmi <= 24.9):
        print(f"\nYour bmi is {bmi:.2f}\nYou are a healthy motherfucker\n")
        response = input("Would you like a diet to help gain weight:y/n\n")
        if response == 'y':
            print('List of food to eat through the week')
            break
        else:
            print("Fuck you mehn!!")
            break

    elif (bmi > 24.9) and (bmi < 30):
        print(f"\nYour bmi is {bmi:.2f}\nYou are overweight brother!!\n")
        response = input("Would you like a diet to help gain weight:y/n\n")
        if response == 'y':
            print('List of food to eat through the week')
            break
        else:
            print("Fuck you mehn!!")
            break

    else:
        print(f"\nYour bmi is {bmi:.2f}\nYou are obese dear, work on your weight!!\n")
        response = input("Would you like a diet to help gain weight:y/n\n")
        if response == 'y':
            print('List of food to eat through the week')
            break
        else:
            print("Fuck you mehn!!")
            break