# Python Full Project
import random
import matplotlib.pyplot as mat
import numpy as num
import time

print('''1 -- number guessing game
2 -- emoji converter
3 -- rock paper scissors
4 -- tax calculator
5 -- weight converter
6 -- wordle
7 -- linegrapher
8 -- full line grapher
9 - function practice
''')
big_choice = input("Enter activity number: ")
if big_choice == '1':
    optionss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    computer_choice = random.choice(optionss)
    tries = 0
    try:
        while True:

            user_guess = int(input("Choose a number between 1 and 20: "))
            tries += 1
            if user_guess == computer_choice:
                print("Correct!")
                print(f"It took you {tries} tries!")
                break
            elif user_guess < computer_choice:
                print("Too low!")
            elif user_guess > computer_choice:
                print("Too high!")
            if tries == 5:
                print(f"You are out of tries! The number was {computer_choice}!")
                break
    except ValueError:
        print("Invalid response, please try again.")
elif big_choice == '2':
    message = input("> ")
    words = message.split(' ')
    emojis = {
        ":)": "😄",
        ":(": "😔",
        "Good".lower(): "👍",
        "Morning".lower(): "🌄",
        "Sunshine".lower(): "☀️"

    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)
elif big_choice == '3':
    ROCK = 'r'
    SCISSORS = 's'
    PAPER = 'p'

    emojis = {
        ROCK: '🪨',
        SCISSORS: '✂️',
        PAPER: '📜'
    }
    user_choices = (tuple(emojis.keys()))
    while True:
        def get_user_choice():
            while True:
                user_input = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
                if user_input in user_choices:
                    return user_input
                else:
                    print("Please enter a valid choice.")


        user_input = get_user_choice()
        computer_choice = random.choice(user_choices)

        print(f"You chose {emojis[user_input]}")
        print(f"Computer chose {emojis[computer_choice]}")

        if user_input == computer_choice:
            print("It's a tie!")
        if user_input == ROCK and computer_choice == SCISSORS:
            print("You win!")
        if user_input == SCISSORS and computer_choice == PAPER:
            print("You win!")
        if user_input == PAPER and computer_choice == ROCK:
            print("You win!")
        if user_input == SCISSORS and computer_choice == ROCK:
            print("You lose!")
        if user_input == PAPER and computer_choice == SCISSORS:
            print("You lose!")
        if user_input == ROCK and computer_choice == PAPER:
            print("You lose!")

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            break


elif big_choice == '4':
    user_price = float(input("What was the price of your items?: "))
    user_taxes = float(input("What is the sales tax for your area?: "))
    user_tax = (user_price * user_taxes) / 100 + user_price
    print(f"Your total for today is ${round(user_tax, 2)}!")
elif big_choice == '5':

    weight = float(input("Enter weight: "))
    weight_pounds = weight * 0.45
    weight_pounds = round(weight_pounds, 2)
    weight_kilograms = weight * 2.2
    weight_kilograms = round(weight_kilograms, 2)
    question = input("(L)bs or (K)g: ")
    if question == "L" or question == "l":
        print(f"You are {weight_pounds} kilograms.")
    if question == "K" or question == "k":
        print(f"You are {weight_kilograms} pounds.")
elif big_choice == '6':
    while True:
        word = ["b", "o", "o", "k", "s"]
        options = []

        while True:
            try:
                user_choice = input("Guess a charactor: ")

            except ValueError:
                print("That's not a valid character.")

            if user_choice in word:
                word.remove(user_choice)
                options.append(user_choice)
                print(options)

            elif user_choice not in word:
                print("That charactor is not part of the word! Try again!")

            if len(options) == 5:
                user_second_choice = input("Can you now unscramble the word?").lower()

                if user_second_choice == "books":
                    print("You are correct! The word was books!")

                else:
                    print("You are incorrect! The word was books!")
                    break
                break
elif big_choice == '7':
    starting_coordinate_input = input('Starting coordinate (seperated by comma): ')
    starting_coordinate = starting_coordinate_input.split(',')

    ending_coordinate_input = input('Ending coordinate (seperated by comma): ')
    ending_coordinate = ending_coordinate_input.split(',')

    line_style_input = input('Enter the line style (1: solid, 2: dashed, 3: dotted): ')
    if line_style_input == '1':
        line_style = 'solid'
    elif line_style_input == '2':
        line_style = 'dashed'
    elif line_style_input == '3':
        line_style = 'dotted'

    line_size_input = input('Enter the line size (as 1 being very small and 20 being large): ')
    line_size = str(line_size_input)

    marker_style_input = input('Enter the marker style (1: dot, 2: star, 3: triangle): ')
    if marker_style_input == '1':
        marker_style = 'o'
    elif marker_style_input == '2':
        marker_style = '*'
    elif marker_style_input == '3':
        marker_style = '^'

    xpoints = num.array([starting_coordinate[0], ending_coordinate[0]])
    ypoints = num.array([starting_coordinate[1], ending_coordinate[1]])

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    mat.plot(xpoints, ypoints, linestyle=line_style, marker=marker_style, linewidth=line_size)
    print('Please check the top right of your screen for your graph')
    mat.show()
elif big_choice == '8':
    def line_graph():
        starting_coordinate_input = input('Enter the starting x coordinates (x, x): ')
        starting_coordinate = starting_coordinate_input.split(',')

        ending_coordinate_input = input('Enter the starting y coordinates (y, y): ')
        ending_coordinate = ending_coordinate_input.split(',')

        xpoints = num.array([starting_coordinate[0], ending_coordinate[0]])
        ypoints = num.array([starting_coordinate[1], ending_coordinate[1]])

        marker = input('Enter the line marker: ')
        line_color = input('Enter the line color (r, g, b): ')
        linewidth = int(input('Enter the line width (1 is small and 20 is big): '))
        linestyle = input('Enter the line style (1: solid, 2: dashed, 3: dotted): ')
        if linestyle == '1':
            line_style = '-'
        elif linestyle == '2':
            line_style = '--'
        elif linestyle == '3':
            line_style = ':'

        mat.plot(xpoints, ypoints, marker=marker, color=line_color, linewidth=linewidth, linestyle=line_style)
        mat.show()


    def bar_graph():
        x_axis_labels = input('Enter the x-axis labels (comma separated): ')
        x_axis_labels = x_axis_labels.split(',')

        y_axis_values = input('Enter the y-axis values (comma separated): ')
        y_axis_values = y_axis_values.split(',')
        mat.bar(x_axis_labels, y_axis_values)
        mat.show()


    def histogram():
        x_axis_values = input('Enter the x-axis values (comma separated): ')
        x_axis_values = x_axis_values.split(',')
        mat.hist(x_axis_values)
        mat.show()


    def pie_chart():
        pie_chart_values = input('Enter the values for the pie chart (comma separated): ')
        pie_chart_values = pie_chart_values.split(',')
        labels = [pie_chart_values[i] for i in range(len(pie_chart_values))]
        mat.pie(pie_chart_values, labels=labels)
        mat.show()


    graph_choice = input('Make a (l)ine, (b)ar graph, (h)istogram, or (p)ie chard? ')
    if graph_choice == 'l':
        line_graph()
    elif graph_choice == 'b':
        bar_graph()
    elif graph_choice == 'h':
        histogram()
    elif graph_choice == 'p':
        pie_chart()

elif big_choice == '9':
    print('''
    1 - star_pyramid
    2 - odd number index addition
    3 - positional and keyword arguments
    4 - args and kwargs
    5 - python function practice
    ''')

function_section_input = input('Enter an activity number: ')

if function_section_input == '1':
    def get_brick_spaces(space, brick_count, brick_type):
    space = space * ' '
    brick_count = brick_count * brick_type
    return f'{space}{brick_count}{space}'

def print_pyramid(max_brick_count, brick_type):
    max_spaces_count = (max_brick_count - 1) // 2
    pyramid = ''
    for spaces_count in range(max_spaces_count, -1, -1):
        brick_count = max_brick_count - (2 * spaces_count)
        pyramid += "\n"+get_brick_spaces(spaces_count, brick_count, brick_type)
    return pyramid


def main():
    max_brick_count = int(input('Enter the max brick count: '))
    if max_brick_count % 2 == 0:
        print('Code will not work, please provide an odd number')
        quit()
    brick_type = input('Enter the brick type: ')
    if len(brick_type) != 1:
        print('Invalid brick type')
        quit()
    pyramidblabla = print_pyramid(max_brick_count, brick_type)
    print(pyramidblabla)
main()

elif function_section_input == '2':
    
def is_odd(index):
    if index % 2 != 0:
        return True
    else:
        return False
def print_sum(list):
    return sum(list)



def main():
    input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    odd_number_index_values = []

    for i in range(len(input_list)):
        is_odd(i)
        if is_odd(i):
            odd_number_index_values.append(input_list[i])
    print(print_sum(odd_number_index_values))


main()

elif function_section_input == '3':
    def say_hello(demo1, demo2):
    say_hello = print(f'{demo1} - {demo2}')
    return say_hello

elif function_section_practice == '4':
    def say_hello(*args):
    for name in args: 
        print(f'Hello {name}!')

def print_scores(**kwargs):
    for subject, score in kwargs.items():
        print(f'{subject}: {score}%')

def student_info(*args, **kwargs):
    print(f'Name: {args}')
    print(f'Scores: {kwargs}%')

def build_sandwich(*args, **kwargs):
    print(f'Sandwich ingreidiants: {args}')
    print(f'Extra Toppings: {kwargs}')

def print_scores_2(**kwargs):
    for subject, score in kwargs.items():
        print(f'{subject}: {score}')

elif function_section_input == '5':
    def addition(num1, num2):
    adding = num1 + num2
    return adding
def subtraction(num1, num2):
    subtraction = num1 - num2
    return subtraction
def multiplication(num1, num2):
    multiplication = num1 * num2
    return multiplication
def division(num1, num2):
    division = num1 / num2
    return division
def powers(num1, num2):
    powers = num1 ** num2
    return powers
calculation = input('(a)dd, (s)ubtract, (m)ultiply, (d)ivide, or (p)ower? ')
input_number_1 = int(input('Enter the first number: '))
input_number_2 = int(input('Enter the second number: '))
if calculation == 'a':
    print(addition(input_number_1, input_number_2))
elif calculation == 's':
    print(subtraction(input_number_1, input_number_2))
elif calculation == 'm':
    print(multiplication(input_number_1, input_number_2))
elif calculation == 'd':
    print(division(input_number_1, input_number_2))
elif calculation == 'p':
    print(powers(input_number_1, input_number_2))

# Classes
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

class John(Person):
    def __init__(self, fname, lname, graduationyear):
        super().__init__(fname, lname)
        self.graduationyear = graduationyear
    def printnameandgraduationyear(self):
        print(f'{self.fname} {self.lname} will graduate on {self.graduationyear}')

john = John('John', 'Smith', 2030)
john.printnameandgraduationyear()


# While Loops
i = 0
while i < 6:
    i += 1
    print('a')
    if i == 3:
        continue
    print('b')
else:
    print('i is now greator than 6')


# Polymorphism 1
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print(f'Drive! {self.brand} {self.model}')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print(f'Sail! {self.brand} {self.model}')

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print(f'Fly! {self.brand} {self.model}')

car = Car('Tesla', 'Cybertruck')
boat = Boat('Benetuau', '2025')
plane = Plane('Boeing', '747')
car.move()
boat.move()
plane.move()

#Polymorphism 2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print(f'{self.brand} {self.model}')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

class Plane(Vehicle):
    pass

car = Car('Tesla', 'Cybertruck')
boat = Boat('Beneteau', '2025')
plane = Plane('Boeing', '747')
car.move()
boat.move()
plane.move()

# Math
import math

x = math.ceil(1.5)
y = math.floor(1.5)
print(x)
print(y)

# Regular Expressions (RegEx)
import re

y = 'Super Cool and Awesome!'
x = re.search('^Su..r', y)
print(x.group())

# Try, Except, Else, and Finally
try:
    x = int(input('Enter a number: '))
except ValueError:
    print('Value Error!')
else:
    print('Nothing went wrong')
finally:
    print('Thanks for participating')

# MatPlotLib
import matplotlib.pyplot as mat
import numpy as np
import time

starting_coordinate_input = input('Starting coordinate (seperated by comma): ')
starting_coordinate = starting_coordinate_input.split(',')

ending_coordinate_input = input('Ending coordinate (seperated by comma): ')
ending_coordinate = ending_coordinate_input.split(',')
xpoints = np.array([starting_coordinate[0], ending_coordinate[0]])
ypoints = np.array([starting_coordinate[1], ending_coordinate[1]])

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

mat.plot(xpoints, ypoints)
print('Please check the top right of your screen for your graph')
mat.show()

# MatPlotLib Full Project
import matplotlib.pyplot as mat
import numpy as num

def line_graph():
    starting_coordinate_input = input('Enter the starting x coordinates (x, x): ')
    starting_coordinate = starting_coordinate_input.split(',')

    ending_coordinate_input = input('Enter the starting y coordinates (y, y): ')
    ending_coordinate = ending_coordinate_input.split(',')

    xpoints = num.array([starting_coordinate[0], ending_coordinate[0]])
    ypoints = num.array([starting_coordinate[1], ending_coordinate[1]])

    marker = input('Enter the line marker: ')
    line_color = input('Enter the line color (r, g, b): ')
    linewidth = int(input('Enter the line width (1 is small and 20 is big): '))
    linestyle = input('Enter the line style (1: solid, 2: dashed, 3: dotted): ')
    if linestyle == '1':
        line_style = '-'
    elif linestyle == '2':
        line_style = '--'
    elif linestyle == '3':
        line_style = ':'

    mat.plot(xpoints, ypoints, marker=marker, color=line_color, linewidth=linewidth, linestyle=line_style)
    mat.show()

def bar_graph():
    x_axis_labels = input('Enter the x-axis labels (comma separated): ')
    x_axis_labels = x_axis_labels.split(',')

    y_axis_values = input('Enter the y-axis values (comma separated): ')
    y_axis_values = y_axis_values.split(',')
    mat.bar(x_axis_labels, y_axis_values)
    mat.show()

def histogram():
    x_axis_values = input('Enter the x-axis values (comma separated): ')
    x_axis_values = x_axis_values.split(',')
    mat.hist(x_axis_values)
    mat.show()

def pie_chart():
    pie_chart_values = input('Enter the values for the pie chart (comma separated): ')
    pie_chart_values = pie_chart_values.split(',')
    labels = [pie_chart_values[i] for i in range(len(pie_chart_values))]
    mat.pie(pie_chart_values, labels=labels)
    mat.show()


graph_choice = input('Make a (l)ine, (b)ar graph, (h)istogram, or (p)ie chard? ')
if graph_choice == 'l':
    line_graph()
elif graph_choice == 'b':
    bar_graph()
elif graph_choice == 'h':
    histogram()
elif graph_choice == 'p':
    pie_chart()

# Function Practice #1

def is_odd(index):
    if index % 2 != 0:
        return True
    else:
        return False
def print_sum(list):
    return sum(list)



def main():
    input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    odd_number_index_values = []

    for i in range(len(input_list)):
        is_odd(i)
        if is_odd(i):
            odd_number_index_values.append(input_list[i])
    print(print_sum(odd_number_index_values))


main()

# Function Practice #2
operation_choice = input('Do you want to add, subtract, multiply, divide or power? ')
numb1 = int(input('Enter the first number: '))
numb2 = int(input('Enter the second number: '))
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2


match operation_choice:
    case 'add':
        print(add(numb1, numb2))
    case 'subtract':
        print(subtract(numb1, numb2))
    case 'multiply':
        print(multiply(numb1, numb2))
    case 'divide':
        print(divide(numb1, numb2))
    case 'power':
        print(power(numb1, numb2))

# Function Practice #3
def addition(num1, num2):
    adding = num1 + num2
    return adding
def subtraction(num1, num2):
    subtraction = num1 - num2
    return subtraction
def multiplication(num1, num2):
    multiplication = num1 * num2
    return multiplication
def division(num1, num2):
    division = num1 / num2
    return division
def powers(num1, num2):
    powers = num1 ** num2
    return powers
calculation = input('(a)dd, (s)ubtract, (m)ultiply, (d)ivide, or (p)ower? ')
input_number_1 = int(input('Enter the first number: '))
input_number_2 = int(input('Enter the second number: '))
if calculation == 'a':
    print(addition(input_number_1, input_number_2))
elif calculation == 's':
    print(subtraction(input_number_1, input_number_2))
elif calculation == 'm':
    print(multiplication(input_number_1, input_number_2))
elif calculation == 'd':
    print(division(input_number_1, input_number_2))
elif calculation == 'p':
    print(powers(input_number_1, input_number_2))

# Function Practice #4

def is_odd(index):
    if index % 2 != 0:
        return True
    else:
        return False
def print_sum(list):
    return sum(list)



def main():
    input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    odd_number_index_values = []

    for i in range(len(input_list)):
        is_odd(i)
        if is_odd(i):
            odd_number_index_values.append(input_list[i])
    print(print_sum(odd_number_index_values))


main()

# Function Practice #5
import math

def findareaofcircle(radius):
    area = math.pi * radius ** 2
    return area

def findcircumferenceofcircle(radius):
    circumference = 2 * math.pi * radius
    return circumference

radiusofcircle = int(input('Enter the radius of your circle: '))
operationchoice = input('Do you want to find the (a)rea of (c)ircumference of your circle? ')
if operationchoice == 'a':
    print(findareaofcircle(radiusofcircle))

elif operationchoice == 'c':
    print(findcircumferenceofcircle(radiusofcircle))

# Function Practice #6
def split_input(input):
    return input.split()

def starting_with(letter, list):
    if list[0] == letter:
        return 'True'
    else:
        return 'False'

name1 = input('Enter a name: ')
name2 = input('Enter another name: ')
name3 = input('Enter a third name: ')
name4 = input('Enter a fourth name: ')
name5 = input('Enter a fifth name: ')
name6 = input('Enter a sixth name: ')
what_letter = input('What letter do you want to know if the word starts with? ')

split_input(name1)
print(starting_with(what_letter, name1))

split_input(name2)
print(starting_with(what_letter, name2))

split_input(name3)
print(starting_with(what_letter, name3))

split_input(name4)
print(starting_with(what_letter, name4))

split_input(name5)
print(starting_with(what_letter, name5))

split_input(name6)
print(starting_with(what_letter, name6))

# Function Practice #7
def get_brick_spaces(space, brick_count, brick_type):
    space = space * ' '
    brick_count = brick_count * brick_type
    return f'{space}{brick_count}{space}'

def print_pyramid(max_brick_count, brick_type):
    max_spaces_count = (max_brick_count - 1) // 2
    pyramid = ''
    for spaces_count in range(max_spaces_count, -1, -1):
        brick_count = max_brick_count - (2 * spaces_count)
        pyramid += "\n"+get_brick_spaces(spaces_count, brick_count, brick_type)
    return pyramid


def main():
    max_brick_count = int(input('Enter the max brick count: '))
    if max_brick_count % 2 == 0:
        print('Code will not work, please provide an odd number')
        quit()
    brick_type = input('Enter the brick type: ')
    if len(brick_type) != 1:
        print('Invalid brick type')
        quit()
    pyramidblabla = print_pyramid(max_brick_count, brick_type)
    print(pyramidblabla)
main()


# Split Function
def split_by_whitespace():
    input_str = 'Sachin    Eshan  Rohan Monika'
    split_result = input_str.split()
    for i in range(len(split_result)):
        print(split_result[i])
def split_by_comma():
    input_str = '1,2,3,4,5'
    split_results = input_str.split(',')
    print(split_results)



def sentence_reverser():
    input_sentence = input('Enter a sentence: ')
    split_input = input_sentence.split()
    list_ending_value_index = len(split_input) - 1
    for i in range(len(split_input) - 1, -1, -1):
        print(split_input[i], end=' ')


def repeating_word_finder():
    jack_counter = 0
    input_story = 'Jack was a curious boy who loved robots. One day, Jack found a dusty toolbox in his attic. Jack used it to build a tiny robot friend named Spark. Every night, Jack and Spark would stargaze and dream of space adventures. Jack knew one day, he and Spark would fly to the stars.'.lower()
    split_input = input_story.split()
    for i in range(len(split_input)):
        if split_input[i] == 'jack':
            jack_counter = jack_counter + 1
    print(jack_counter)

def repeating_word_finder_advanced():
    jack_counter = 0
    input_story = input('Enter a story (3-4 lines) ').lower()
    word_to_find = input('What word would you like to find in your story? ').lower()
    word_is_valid = word_to_find.split()
    
    if len(word_is_valid) == 1: 
        split_input = input_story.split()
        for i in range(len(split_input)):
            if split_input[i] == word_to_find:
                jack_counter = jack_counter + 1
        print(jack_counter)
    else:
        print('You can only find one word!')
    
repeating_word_finder_advanced()

# *args and **kwargs #1
def say_hello(*args):
    for name in args: 
        print(f'Hello {name}!')

def print_scores(**kwargs):
    for subject, score in kwargs.items():
        print(f'{subject}: {score}%')

def student_info(*args, **kwargs):
    print(f'Name: {args}')
    print(f'Scores: {kwargs}%')

def build_sandwich(*args, **kwargs):
    print(f'Sandwich ingreidiants: {args}')
    print(f'Extra Toppings: {kwargs}')

def print_scores_2(**kwargs):
    for subject, score in kwargs.items():
        print(f'{subject}: {score}')

# Function Practice #8
def farenheit_to_celsius(degree):
    converted_celsius = print((degree - 32) * 5/9)
    return converted_celsius

def celsius_to_farenheit(degree):
    converted_farenheit = print((degree * 9/5) + 32)
    return converted_farenheit

temperature_input = int(input('Enter a temperature: '))
conversion_input = input('(F)arenheit or (C)elsius: ').lower()
if conversion_input == 'f':
    farenheit_to_celsius(temperature_input)

elif conversion_input == 'c':
    celsius_to_farenheit(temperature_input)

else:
    print('Invalid Input!')
    
# Filter, Map and Lambda
def cel_to_far():
    temp_c = [0,20,7,14,12]
    temp_f = list(map(lambda cel: (cel * 9/5) + 32, temp_c))
    print(temp_f)

def find_evens():
    nums = [0,1,2,3,4,5,6,7,8,9]
    evens = list(filter(lambda even: even % 2 == 0, nums))
    print(*evens)

def find_long_words():
    words = ['hi', 'hello', 'wazzup', 'hey', 'howyadoin']
    long_words = list(filter(lambda word: len(word) >= 4, words))
    print(*long_words)

# *args and **kwargs #2
def even_number_seperator():
    nums = [1,2,3,4,5,6]
    evens = list(filter(lambda num: num % 2 == 0, nums))
    print(evens)

# even_number_seperator()

def sandwich_builder(*args, **kwargs):
    for topping in args:
        print((f'You chose for topping: {topping}'))
    for choice_of_sauce in kwargs:
        print(f'Your choice of sauce was: {choice_of_sauce}')

# sandwich_builder('Premium Chicken', "Jalepeno's", 'Black Olives', choice_of_sauce = 'Normal Tomato Sauce')

def pizza_builder(*toppings):
    for topping in toppings:
        print(f'🍕 {topping}')

# pizza_builder('Premium Chicken', "Jalepeno's", 'Black Olives')

def character_builder(**kwargs):
    for key, value in kwargs.items():
        print(f'🧙‍♂️ {key}: {value}')

# character_builder(name='Eshan the Great', age=13, class_='Wizard', power='smart')

def shopping_list(*args, **kwargs):
    for item in args:
        if item in kwargs:
            print(f'{item}: ${kwargs[item]}')
        else: 
            print(f'{item}: No Price Added')

# shopping_list('apple', 'banana', 'blueberries', 'grapes', apple=1, banana=2, blueberries=1.5, grapes=2)

    















