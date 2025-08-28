import math
import random

def area_of_square():
    side_length = int(input('Enter the side length of the square: '))
    print(f'The area of the square is: {side_length ** 2}!')

#area_of_square()


def area_and_perimeter_finder():
    length = int(input('Enter the length of the rectangle: '))
    width = int(input('Enter the width of the rectangle: '))
    area = length * width
    perimeter = (length * 2) + (width * 2)
    print(f'The area is {area} and the perimeter is {perimeter}!')

#area_and_perimeter_finder()

def area_and_circumference_finder():
    PI = 3.142
    radius_of_circle = int(input('Enter the radius of the circle: '))
    area = int(PI * (radius_of_circle ** 2))
    circumference = int(PI * (radius_of_circle * 2))
    print(f'The area is {area} and the circumference is {circumference}!')

#area_and_circumference_finder()

def surface_area_cost_finder():
    side_lengths_input = input('Enter the side lengths (seperated by comma): ')
    side_lengths = side_lengths_input.split(',')
    cost_per_unit = float(input('Enter the cost per unit of surface area: '))
    length = int(side_lengths[0])
    width = int(side_lengths[1])
    height = int(side_lengths[2])
    surface_area = 2 * (length * width + width * height + height * length)
    final_cost = surface_area/cost_per_unit
    math.ceil(final_cost)
    print(f'The final cost is ${final_cost}!')

#surface_area_cost_finder()

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


#body_mass_index_finder()

def quadratic_function_calculater():
    value_a = int(input('Enter a value for A: '))
    value_b = int(input('Enter a value for B: '))
    value_c = int(input('Enter a value for C: '))
    discriminant = (value_b ** 2) - (4 * value_a * value_c)
    first_root = (-1 * value_b + (discriminant ** 0.5)) / (2 * value_a)
    second_root = (-1 * value_b - (discriminant ** 0.5)) / (2 * value_a)
    print(f'The first root is {first_root} and the second root is {second_root}!')
#quadratic_function_calculater()

def hyperbola_foci_verticies_calculater():
    vertical_horizontal_input = input('Is the hyperbola horizontal or vertical? ').lower()
    if vertical_horizontal_input == 'horizontal':
        vertex_input = input('Enter the vertex of the hyperbola seperated by comma: ')
        vertex = vertex_input.split(',')
        vertex_h = int(vertex[0])
        vertex_k = int(vertex[1])
        value_a = int(input('Enter the value of A: '))
        value_c = int(input('Enter the value fo C: '))
        print(f'The foci of the hyperbola is (+-{value_c + vertex_h}, {vertex_k})')
        print(f'The verticies of the hyperbola is (+-{value_a + vertex_h}, {vertex_k})')
    
    elif vertical_horizontal_input == 'vertical':
        vertex_input = input('Enter the vertex of the hyperbola seperated by comma: ')
        vertex = vertex_input.split(',')
        vertex_h = int(vertex[0])
        vertex_k = int(vertex[1])
        value_a = int(input('Enter the value of A: '))
        value_c = int(input('Enter the value fo C: '))
        print(f'The foci of the hyperbola is ({vertex_h}, +-{value_c + vertex_k})')
        print(f'The verticies of the hyperbola is ({vertex_h}, +-{value_a + vertex_k})')
    
#hyperbola_foci_verticies_calculater()

def joining_strings():  
    print('Hi Person'[:2] + ' Eshan')
#joining_strings()
def reversing_strings():
    print('Hello! My name is Eshan!' [::-1])
#reversing_strings()

def replace_input_word():
    input_sentence = input('Enter a sentence: ')
    word_to_replace = input('Which word or part would you like to replace: ')
    replacing_word = input('What word or sentence would you like to replace that word with: ')
    print(input_sentence.replace(word_to_replace, replacing_word))

#replace_input_word()

def verify_supplier():
    supplier_name = input('What is the name of the supplier that you use: ').lower()
    if supplier_name == 'gell' or supplier_name == 'tompaq':
        print('You are using a verified supplier!')
    else:
        print('You are not using a verified supplier!')

#verify_supplier()

def sales_tax_applicable_checker():
    state = input('Which state do you live in: ').lower()
    price = int(input('What is your total price: '))
    if state == 'Florida' or price <= 9:
        print('Sales tax applicable')
    if state == 'New York' or price<= 9:
        print('Sales tax applicable')
    if state == 'Texas' or price <= 12:
        print('Sales tax applicable')
    else:
        print('Only local taxes applicable')

#sales_tax_applicable_checker()

def password_guesser():
    password = 'p4s$'
    for i in range(3):
        password_guess = input('Enter the password: ')
        if password_guess != password:
            print('Access Denied')
        else:
            print('Access Granted')

#password_guesser()
        
def division(num1, num2):
    if num2 == 0:
        print('Infinity')
    else:
        print(num1/num2)

#division(3,0)

def print_from_num_to_num(starting, ending, increment):
    for i in range(starting, ending, increment):
        print(i)

#print_from_num_to_num(20, 31, 1)

def print_even_numbers():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    even_numbers = []
    for i in range(len(numbers)):
        if len(even_numbers) != 5:
            if i % 2 == 0:
                even_numbers.append(i)
        
    print(even_numbers)

#print_even_numbers()

def find_tallest_height():
    max_height = 1
    height = int(input('Enter a height in inches [enter 0 to quit]: '))
    while(height != 0):
        height = int(input('Enter a height in inches [enter 0 to quit]: '))
        if height > max_height:
            max_height = height 
    print(f'The max height was {max_height}')
    

#find_tallest_height()

def find_prime_number():
    is_prime = True
    input_number = int(input('Enter a number: '))
    ending_factor = int((input_number ** 0.5) + 1)
    for i in range(2, ending_factor):
        if input_number % i == 0:
            is_prime = False
    if is_prime:
        print('The number is a prime number! 🟢')
    else:
        print('The number is not prime! 🔴')

#find_prime_number()

def split_apples_to_students():
    apples = int(input('Enter the number of apples: '))
    students = int(input('Enter the number of students: '))
    if apples % students == 0:
        print(f'Each student will receive {int(apples/students)} apples!')
    else:
        print(f'Each student will receive {apples//students} apples, but there will be {apples%students} remaining.')

#split_apples_to_students()

def print_random_numbers():
    numbers_printed = []
    for i in range(101):
        if len(numbers_printed) == 20:
            print(numbers_printed)
            break
        else:
            random_number = random.randint(1, 100)
            numbers_printed.append(random_number)

#print_random_numbers()

def greet_me(name=input('Enter your name: ')):
    greet = print(f'Hello {name}')
    return greet

#greet_me()

def give_measurments():
    findarea(shape='circle', radius=int(input('Enter the radius ')))
    findarea(shape='rectangle', height=int(input('Enter the height: ')), length=int(input('Enter the length: ')))
    findarea(shape='square', side=int(input('Enter the side length: ')))

def findarea(shape='none', radius=0, height=0, length=0, side=0):
    if shape == 'circle':
        area = math.pi * (radius ** 2)
        print(f'The area of the {shape} is: {area}')
    elif shape == 'rectangle':
        area = length * height
        print(f'The srea of the {shape} is: {area}')
    elif shape == 'square':
        area = side ** 2
        print(f'The area of the {shape} is: {area}')

#give_measurments()

def guess_the_number():
    number = random.randint(1, 100)
    guessed_numbers = []
    for guesses in range(8):
        if guesses == 8:
            print(f'You lost! The number was {number}!')
            break
        else:
            guess = int(input('Enter a number: '))
            if guess in guessed_numbers:
                print('You already guessed that! Try again!')
            else:
                if guess > number:
                    print('Too high!')
                    guessed_numbers.append(guess)
                elif guess < number:
                    print('Too low!')
                if guess == number:
                    print(f'You win! The number was {number}!')

#guess_the_number()


    
    
        


                                     