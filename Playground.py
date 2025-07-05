def body_mass_index_finder():
    weight_in_lbs = int(input('Enter your weight in lbs: '))
    height_in_inches = int(input('Enter your height in inches: '))
    body_mass_index = int((weight_in_lbs * 703)/(height_in_inches**2))
    if body_mass_index < 14:
        print(f'Your BMI is {body_mass_index}. You are underweight.')
    elif body_mass_index >= 14 and body_mass_index <= 24:
        print(f'Your BMI is {body_mass_index}. You have ideal weight.')
    elif body_mass_index > 29:
        print(f'Your BMI is {body_mass_index}. You are obese.')


body_mass_index_finder()