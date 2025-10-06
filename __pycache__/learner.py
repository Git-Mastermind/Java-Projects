# Python Full Project
import random
import matplotlib.pyplot as mat
import numpy as num
import time
import math
import requests
import json
import mysql.connector
from decimal import Decimal
import pandas as pd


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

if function_section_input == '2':
    
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

elif function_section_input == '4':
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
def advanced_calculator():
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

def starting_letter_finder():
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

# Python book coding problems
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

# Pandas

def ages_to_names():
    ages = pd.Series([12,13,14], index=['Eshan', 'Ali', 'Lily'])
    print(ages)

# ages_to_names()

def cars_model_dataset():
    cars_model = {
        'cars' : ['Tesla', 'Rivian', 'Range Rover'],
        'model' : ['Cybertruck', 'R1S', 'Land Rover']
    }
    cars_model_dataframe = pd.DataFrame(cars_model)
    print(cars_model_dataframe)

# cars_model_dataset()

def fruit_series():
    fruits = ['apples', 'strawberries', 'blueberries', 'cherries', 'grapes']
    series = pd.Series(fruits, index=['a', 'b', 'c', 'd', 'e'])
    print(series)

# fruit_series()

def dictionary_series():
    calories = {'day1':300, 'day2':400, 'day3':600}
    calorie_series = pd.Series(calories, index=['day1', 'day2', 'day3'])
    print(calorie_series)
    
# dictionary_series()

def pandas_dataframes():
    calorie_data = {
        'calories' : [500, 502, 600, 700, 420, 501],
        'duration' : [47, 46, 56, 63, 39, 43]
    }
    calorie_duration_dataframed = pd.DataFrame(calorie_data)
    print(calorie_duration_dataframed)

# pandas_dataframes()

def pandas_read_csv():
    df = pd.read_csv('data.csv')
    print(df)

pandas_read_csv()

# For printing max rows avalile:
#   print(pd.options.display.max_rows)

def pandas_clean_cells():
    df = pd.read_csv('data.csv')
    df.dropna(inplace=True)
    print(df.to_string())

# pandas_clean_cells()

# factorial_calculator
def factorial_calculator(number):
    if number < 0:
        print('Factorial is not defined for negative integers!')
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        if result > 10000000000:
            raise ValueError("Input exceeds allowable capacity.")
            raise ValueError("Operation attempted with excessive load.")
            raise ValueError("The provided argument surpasses permissible limits.")
        else:
            return print(result)

number = int(input('Enter a number: '))
factorial_calculator(number)

# Requests Module Learning

def random_user_information():
    random_user = requests.get('https://randomuser.me/api/')
    data = random_user.json()
    json.dumps(data, indent=2)
    user = data['results'][0]
    first_name = user['name']['first']
    last_name = user['name']['last']
    country = user['location']['country']
    email = user['email']
    phone = user['phone']

    print(f'🤵Name: {first_name} {last_name}')
    print(f'🚩Country: {country}')
    print(f'📩Email: {email}')
    print(f'📱Phone: {phone}')

# random_user_information()

def random_joke():
    random_joke = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = random_joke.json()
    json.dumps(data, indent=2)
    joke = data['setup']
    punchline = data['punchline']
    print(f'{joke}')
    time.sleep(3)
    print(f'{punchline}')    

# random_joke()

def motivational_quote_getter():
    random_quote = requests.get('https://zenquotes.io/api/random')
    data = random_quote.json()
    quote = data[0]['q']
    by_who = data[0]['a']
    print(f'{quote} - {by_who}')


# motivational_quote_getter()

def post_blog_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title':"Eshan's Coding Blog",
        'body':'I coded today, and it felt magical!',
        'userId':13
    }

    post = requests.post(url, json=data)

    if post.status_code == 201:
        print('✅Everything went well!')
    else:
        print('❌Something went wrong!')
# post_blog_data()

def topic_related_jokes():
    url_categories = {
        'general':'https://official-joke-api.appspot.com/jokes/general/random',
        'programming':'https://official-joke-api.appspot.com/jokes/programming/random',
        'knock-knock':'https://official-joke-api.appspot.com/jokes/knock-knock/random'
    }
    type_of_joke = input('Enter the type of joke (general, programming or knock-knock): ').lower()
    if type_of_joke == 'general':
        data = requests.get(url_categories['general']).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)

    elif type_of_joke == 'programming':
        data = requests.get(url_categories['programming']).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)
    
    elif type_of_joke == 'knock-knock' or type_of_joke == 'knock knock':
        data = requests.get(url_categories['knock-knock']).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)


# topic_related_jokes()

def topic_related_jokes_cleanedup():
    url_categories = {
        'general':'https://official-joke-api.appspot.com/jokes/general/random',
        'programming':'https://official-joke-api.appspot.com/jokes/programming/random',
        'knock-knock':'https://official-joke-api.appspot.com/jokes/knock-knock/random'
    }
    type_of_joke = input('Enter the type of joke (general, programming, or knock-knock): ').lower()
    if type_of_joke == 'knock knock':
        type_of_joke = 'knock-knock'
    if type_of_joke in url_categories:
        data = requests.get(url_categories[type_of_joke]).json()
        joke = data[0]['setup']
        punchline = data[0]['punchline']
        print(joke)
        time.sleep(2)
        print(punchline)
# topic_related_jokes_cleanedup()

def check_github_stats():
    username = input('Enter your github username: ')
    url_repo = f'https://api.github.com/users/{username}/repos'
    url_info = f'https://api.github.com/users/{username}'
    repos = requests.get(url_repo)
    info = requests.get(url_info)
    if repos.status_code == 200 and info.status_code == 200:

        repo_data = repos.json()
        info_data = info.json()
        repo_name = repo_data[0]['name']
        profile_link = repo_data[0]['url']
        name = info_data['name']
        following = info_data['following']
        followers = info_data['followers']
        print(f'💻 Username: {username}')
        print(f'🌐 Profile Link: {profile_link}')
        print(f'🧠 Repo: {repo_name}')
        print(f'👋 Name: {name}')
        print(f'🙏 Following: {following}')
        print(f'👈 Followers: {followers}')
        print('✅ Everything went smoothly!')
    else:
        print(f'❌ Something went wrong: {info.status_code}')


# check_github_stats()

def check_name():
    username = input('Enter username: ')
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"✅The user's name is {data['name']}"
    else:
        return f"❌Something went wrong: {response.status_code}"


# print(check_name())

def country_facts_lookup():
    country = input('Enter a country: ')
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        common_name = data[0]['name']['common']
        official_name = data[0]['name']['official']
        capital = data[0]['capital'][0]
        region = data[0]['region']
        population = data[0]['population']
        currencies = data[0]['currencies']
        currency_code = list(currencies.keys())[0]
        languages = data[0]['languages']
        language = list(languages.values())
        flag = data[0]['flag']
        print(f'🌍 Country: {common_name}')
        print(f'🤝 Official Name: {official_name}')
        print(f'🏛️ Capital: {capital}')
        print(f'🌐 Region: {region}')
        print(f'🧑‍🤝‍🧑 Population: {population}')
        print(f'💰 Currency: {currency_code}')
        print(f'🗣️ Language: {language}')
        print(f'🚩 Flag: {flag}')
        print('✅ Everything went smoothly!')
    else:
        print(f'❌ Something went wrong: {response.status_code}')


# country_facts_lookup()

def animal_rescue():
    animal_name = input('Enter animal name: ')
    animal_type = input('Enter animal type: ')
    data = {
        'name':animal_name,
        'type':animal_type
    }
    post = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
    print(post.json())
    if post.status_code == 201:
        print('✅ Animal Rescued Successfully!')
    else:
        print(f'❌ Something went wrong: {post.status_code}')

# animal_rescue()

def pet_adoption_form():
    print('👋 Welcome to the Pet Adoption Center!')
    name = input("What's your name? ")
    animal = input('WHat kind of pet would you like to adopt? ')
    data = {
        'name':name,
        'animal':animal
    }
    url = 'https://jsonplaceholder.typicode.com/posts'
    post = requests.post(url, json=data)
    if post.status_code == 201:
        print(f'✅ Thanks {name}! Your request to adopt a {animal} has been submitted!')
        see_code = input('Would you like to see? ').lower()
        if see_code == 'yes':
            print(post.json())
        else:
            print('Good Bye!')

# pet_adoption_form()

def dragon_registration_system():
    print('🐉 Welcome to Dragon Registration System!')
    dragon_name = input("Enter dragon name: ")
    dragon_type = input("Enter dragon type: ")
    power_level = int(input("Enter power level: "))
    license_color = input('Choose license color(gold, silver bronze): ').lower()
    if 1 <= power_level <= 100:
        if license_color == 'gold' or license_color == 'silver' or license_color == 'bronze':
            data = {
                'dragon_name' : dragon_name,
                'dragon_type' : dragon_type,
                'power' : power_level,
                'license' : license_color
            }
            url = 'https://jsonplaceholder.typicode.com/posts'
            post = requests.post(url, json=data)
            if post.status_code == 201:
                print('✅ Dragon registered successfully!')
                see_code = input('Would you like to see the receipt? ').lower()
                if see_code == 'yes':
                    print(post.json())
                else:
                    print('GoodBye!')
            else:
                print('❌ Something went wrong')
        else:
            print('Invalid license color!')
    else:
        print('Invalid power level domain!')

# dragon_registration_system()

def dragon_registration_system_cleanedup():
    print('🐉 Welcome to Dragon Registrion System!')
    dragon_name = input('Enter dragon name: ')
    dragon_type = input('Enter dragon type: ')
    while True:
        try:
            power_level = int(input('Enter power level(1-1000): '))
            if 1 <= power_level <= 1000:
                break
            else:
                print('❌ Invalid Domain! Please try again!')
        except ValueError:
            print('❌ Invalid Input! Please try again!')
    valid_license_colors = ['gold', 'silver', 'bronze']
    while True:
        license_color = input('Enter license color(gold, silver, bronze): ').lower()
        if license_color in valid_license_colors:
            break
        else:
            print('❌ Invalid license color! Please try again!')
    data = {
        'dragon_name':dragon_name,
        'dragon_type':dragon_type,
        'license_color':license_color,
        'power_level':power_level
    }
    url = 'https://jsonplaceholder.typicode.com/posts'
    post_info = requests.post(url, json=data)
    if post_info.status_code == 201:
        print('✅ Dragon Registered Successfully!')
        see_code = input('Would you like to see the receipt? ').lower()
        if see_code == 'yes':
            print(post_info.json())
        else:
            print('GoodBye!')
    else:
        print(f'❌ Something went wrong: {post_info.status_code}')


# dragon_registration_system_cleanedup()

def update_data():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    updated_info = {
        'userId':1,
        'Id':1,
        'title':'updating this post!',
        'body':'This is the updated content of the post'
    }
    put_info = requests.put(url, json=updated_info)
    print(put_info.text)
    if put_info.status_code == 200:
        print(f'✅ Everything went smoothly: {put_info.status_code}')
    else:
        print(f'❌ Something went wrong: {put_info.status_code}')

# update_data()

def delete_data():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    delete_data = requests.delete(url)
    print(delete_data.text)
    if delete_data.status_code == 200:
        print(f'✅ Everything went smoothly: {delete_data.status_code}')
    else:
        print(f'❌ Something went wrong: {delete_data.status_code}')

# delete_data()

def update_rocket_info():
    url = 'https://jsonplaceholder.typicode.com/posts/2'
    data = {
        'userId':2,
        'Id':2,
        'title':'Updated info on rocket',
        'body':'need more rocket fuel, less liquid methane pls'
    }
    update_info = requests.put(url, json=data)
    print(update_info.text)
    if update_info.status_code == 200:
        print(f'✅ Everything went smoothly: {update_info.status_code}')
    else:
        print(f'❌ Something went wrong: {update_info.status_code}')

# update_rocket_info()

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="eshanjha",
    password="ILovebooks!@#123",
    database="enu_db"
)
print('Initializing Database...')
time.sleep(0.8)
print('Connected to mySQL!')
time.sleep(0.3)

cursor = connection.cursor()
def fetchall(query):
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)


# def fetch(query):
#     cursor.execute(query)
#     cursor.fetchall()
def fetch(query):
    cursor.execute(query)
    results = cursor.fetchall()  # always returns a list of tuples
    clean_results = []

    # convert any Decimals to float
    for row in results:
        clean_row = tuple(float(x) if isinstance(x, Decimal) else x for x in row)
        clean_results.append(clean_row)

    return clean_results



def run_action(query):
    cursor.execute(query)
    connection.commit()

def switch_database(database):
    connection = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="eshanjha",
    password="ILovebooks!@#123",
    database=database)
    return f"you are currently using {database}"

switch_database('sql_store')


def apartment_renter_managment():
    logged_in = False
    renter_id = 0

    def log_in():
        nonlocal renter_id, logged_in
        time.sleep(0.3)

        renter_id = int(input('Enter your renter id: '))
        results = fetch(f'SELECT first_name, last_name FROM renters WHERE renter_id = {renter_id}')

        if results:
            print('Fetching Data from Database...')
            time.sleep(1.5)
            print(f'✅ Welcome {results[0][0]} {results[0][1]}')
            logged_in = True
            time.sleep(2)

        else:
            print('❌ Renter ID not found')
    
    def sign_up():
        print('Please enter your credentials')
        time.sleep(0.3)

        first_name = input('First Name: ')

        last_name = input('Last Name: ')

        phone_number = input('Phone Number: ')

        email = input('Email: ')

        apartment_number = input('Which apartment do you want to buy (type help for available apartments): ')

        if apartment_number == 'help' or apartment_number == 'HELP':
            avab_apartments = fetch(f"SELECT apartment_number FROM apartments WHERE is_available = 1")
            avab_apartments = [apt[0] for apt in avab_apartments]

            print(f"🏠 Available Apartments: {avab_apartments}")

            apartment_number = input('Which apartment do you want to buy: ')

            move_in_date = input('When will you move in: ')

            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")

            new_renter_id = fetch(f"SELECT r.renter_id FROM apartments a LEFT JOIN renters r USING (apartment_number) WHERE apartment_number = '{apartment_number}'")

            run_action(f"UPDATE apartments SET is_available = 0 WHERE apartment_number = '{apartment_number}'")
            print('Fetching Data...')
            time.sleep(0.3)

            print('Inserting Data Into Table...')
            time.sleep(0.2)

            print('Fetching Renter ID...')
            time.sleep(0.2)

            print(f'✅ Successfully Signed Up! Your renter id is {new_renter_id[0][0]}')

        else:
            move_in_date = input('When will ou move in: ')

            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")

            new_renter_id = run_action(f'SELECT renter_id FROM apartments WHERE apartment_number = {apartment_number}')
            new_renter_id = [renter_id_new[0] for renter_id_new in new_renter_id]

            print(f'✅ Successfully Signed Up! Your renter id is {new_renter_id[0][0]}!')

    def apartment_stats():
        apartment_number = input('Apartment Number (type help for available apartments): ')
        if apartment_number == 'help':
            avab_apartments = fetch(f"SELECT apartment_number FROM apartments WHERE is_available = 1")
            avab_apartments = [apt[0] for apt in avab_apartments]
            print(f'🏠 Available Apartments = {avab_apartments}')
            apartment_number = input('Apartment Number: ')
            apartment_info = fetch(f"SELECT bedrooms, bathrooms, rent_amount FROM apartments WHERE apartment_number = '{apartment_number}'")
            bedrooms = apartment_info[0][0]
            bathrooms = apartment_info[0][1]
            rent_amount = apartment_info[0][2]
            print(f'🛏️ Bedrooms: {bedrooms}')
            print(f'🧻 Bathrooms: {bathrooms}')
            print(f'💵 Rent: {rent_amount}')

        else:
            apartment_info = fetch(f"SELECT bedrooms, bathrooms, rent_amount FROM apartments WHERE apartment_number = '{apartment_number}'")
            bedrooms = apartment_info[0][0]
            bathrooms = apartment_info[0][1]
            rent_amount = apartment_info[0][2]
            print(f'🛏️ Bedrooms: {bedrooms}')
            print(f'🧻 Bathrooms: {bathrooms}')
            print(f'💵 Rent: {rent_amount}')
            
    def forgot_renter_id():
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        phone_number = input('Phone Number: ')

        renter_id = fetch(f"SELECT renter_id FROM renters WHERE first_name = '{first_name}' AND last_name = '{last_name}' AND phone_number = '{phone_number}'")
        print('Fetching Data...')
        time.sleep(1)

        print(f'✅ Your renter id is {renter_id[0][0]}')
        time.sleep(2)





    
    
    
    def update_renter_info():
        nonlocal renter_id
        time.sleep(0.3)
        # renter_to_update = int(input('Please enter your renter id: '))
        print('Fethcing...')
        time.sleep(0.6)
        info = print('''Update: 
                                1: First Name
                                2: Last Name
                                3: Phone Number
                                4: Email
                                5: Apartment Number''')
        info_to_update = int(input('Choose an option: '))

            
        if info_to_update == 1:
            results = fetch(f'SELECT first_name FROM renters WHERE renter_id = {renter_id}')
            print(f'Original First Name = {results[0][0]}')
            first_name = input('New First Name = ')
            run_action(f"UPDATE renters SET first_name = '{first_name}' WHERE renter_id = {renter_id}")
            print('Updating...')
            time.sleep(0.6)
            print("✅ Successfully Updated First Name!")
            time.sleep(2)

        elif info_to_update == 2:
            results = fetch(f"SELECT last_name FROM renters WHERE renter_id = {renter_id}")
            print(f'Original Last Name = {results[0][0]}')
            last_name = input('New Last Name = ')
            run_action(f"UPDATE renters SET last_name = '{last_name}' WHERE renter_id = {renter_id}")
            print('Updating...')
            time.sleep(0.6)
            print("✅ Successfully Updated Last Name!")
            time.sleep(2)

        elif info_to_update == 3:
            results = fetch(f'SELECT phone_number FROM renters WHERE renter_id = {renter_id}')
            print(f'Original Phone Number = {results[0][0]}')
            phone_number = input('New Phone Number (xxx-xxx-xxxx) = ')
            run_action(f"UPDATE renters SET phone_number = '{phone_number}' WHERE renter_id = {renter_id}")
            print('Updating...')
            time.sleep(0.6)
            print("✅ Successfully Updated Phone Number!")
            time.sleep(2)

        elif info_to_update == 4:
            results = fetch(f'SELECT email FROM renters WHERE renter_id = {renter_id}')
            print(f'Original Email = {results[0][0]}')
            email = input('New Email = ')
            run_action(f"UPDATE renters SET email = '{email}' WHERE renter_id = {renter_id}")
            print('Updating...')
            time.sleep(0.6)
            print("✅ Successfully Updated Email!")
            time.sleep(2)

        elif info_to_update == 5:
            results = fetch(f'SELECT apartment_number FROM renters WHERE renter_id = {renter_id}')
            print(f'Original Apartment Number = {results[0][0]}')
            apartment_number = input('New Apartment Number = ')
            is_available = fetch(f"SELECT is_available FROM apartments WHERE apartment_number = '{apartment_number}'")
            if is_available[0][0] == 1:
                run_action(f"UPDATE renters SET apartment_number = '{apartment_number}' WHERE renter_id = {renter_id}")
                run_action(f"UPDATE apartments SET is_available = 0 WHERE apartment_number = '{apartment_number}'")
                run_action(f"UPDATE apartments SET is_available = 1 WHERE apartment_number = '{results[0][0]}'")
                print('Updating...')
                time.sleep(0.6)
                print("✅ Successfully Updated Apartment Number!")
                time.sleep(2)

            else:
                print("❌ That apartment is occupied!")
                
                

        

    def list_apartments():
        time.sleep(0.3)
        avab_apartments = fetch("SELECT apartment_number, rent_amount, bedrooms, bathrooms FROM apartments WHERE is_available = 1")
        avab_apartments = [apt[0] for apt in avab_apartments]

        print('Fetching Data from Database...')
        time.sleep(0.3)

        print('Fetching available apartments')
        time.sleep(0.2)

        print(f"🏠 Available Apartments: {avab_apartments}")
        print('✅ Successfully Fetched Apartments!')
        time.sleep(2)
    
    def list_renters():
        time.sleep(0.3)
        results = fetch("SELECT first_name, last_name, apartment_number FROM renters")
        results = [renters[0] for renters in results]
        print('Fetching Data from Database...')
        time.sleep(0.3)

        print('Fetching All Renters...')
        time.sleep(0.2)

        print(f"🤑 Renters: {results}")
        print('✅ Successfully Fetched Renters!')
        time.sleep(2)
    
    def avg_rent_per_city():
        time.sleep(0.3)
        print('Fetching Data from Database...')
        time.sleep(0.3)

        print('Fetching All Renters...')
        time.sleep(0.2)

        fetchall("SELECT city, AVG(rent_amount) FROM apartments GROUP BY city")
        print('✅ Success')
        time.sleep(2)
    
    def find_renter_by_city():
        time.sleep(0.3)
        input_city = input('Enter a city: ')
        fetchall(f"SELECT r.first_name, r.last_name, a.apartment_number FROM apartments a JOIN renters r USING (apartment_number) WHERE city = '{input_city}'")
        print('✅ Success')
        time.sleep(2)

    
    def insert_apartment():
        time.sleep(0.3)
        print('Enter the credentials')
        time.sleep(0.5)
        apartment_number = input('Apartment Number: ')

        address = input('Address: ')

        city = input('City: ')

        state = input('State: ')

        zip_code = int(input('Zip Code: '))

        rent_amount = int(input('Rent Amount: '))

        bedrooms = int(input('Bedrooms: '))

        bathrooms = int(input('Bathrooms: '))

        avab_check = fetch(f"SELECT apartment_number FROM apartments WHERE apartment_number = '{apartment_number}'")
        if avab_check == apartment_number:
            print(f'❌ Apartment {apartment_number} has already been created!')
        else:
            apartment_query = f"INSERT INTO apartments (apartment_number, address, city, state, zip_code, rent_amount, bedrooms, bathrooms) VALUES ('{apartment_number}', '{address}', '{city}', '{state}', {zip_code}, {rent_amount}, {bedrooms}, {bathrooms})"
            run_action(apartment_query)
            run_action(f"UPDATE apartments SET is_available = 1 WHERE apartment_number = '{apartment_number}'")
            print('Brewing Concrete...')
            time.sleep(0.6)

            print('Building the Walls...')
            time.sleep(0.5)

            print('Adding the Roof...')
            time.sleep(0.3)

            print('Inserting Data into Table...')
            time.sleep(0.6)

            print('✅ Created New Apartment')
            time.sleep(2)

    def get_recommendations():
        max_budget = int(input('Max Budget: '))

        num_of_bedrooms = int(input('Number of Bedrooms: '))

        num_of_bathrooms = int(input('Num of Bathrooms: '))

        results = fetch(f"SELECT apartment_number FROM apartments WHERE rent_amount <= {max_budget} AND bedrooms <= {num_of_bedrooms} AND bathrooms <= {num_of_bathrooms} AND is_available = 1")
        results = [key[0] for key in results]
        print('Fetching Data...')
        time.sleep(0.6)

        print('Inserting Recommendations...')
        time.sleep(0.3)

        print(f"🏠 Recommended Apartments: {results}")
        time.sleep(2)

    
    
    def log_out():
        nonlocal logged_in
        print('Logging out...')
        time.sleep(0.8)

        print('Rebooting Visuals...')
        time.sleep(0.4)

        print('Logged out!')
        time.sleep(0.3)

        logged_in = False
    
    while True:
        if not logged_in:
            print('''----- Apartment and Renter Managment -----
                1: Log In
                2: Buy an Apartment
                3: See Apartment Info
                4: Forgot Renter Id?
                5: Exit''')
            action_input = int(input('Choose an option: '))
            if action_input == 1:
                log_in()
                    
            elif action_input == 2:
                sign_up()

            elif action_input == 3:
                apartment_stats()
            
            elif action_input == 4:
                forgot_renter_id()
            
            elif action_input == 5:
                print('👋 Goodbye!')
                quit()


            
            while logged_in:
                print('''----- Apartment and Renter Managment -----
                    1 ----- Update Renter Info
                    2 ----- List Available Apartments
                    3 ----- List Renters
                    4 ----- Create New Apartment
                    5 ----- Get Recommendations
                    6 ----- Log Out
                    7 ----- Exit''')
                action_input = int(input('Choose an option: '))
                if action_input == 1:
                    update_renter_info()

                elif action_input == 2:
                    list_apartments()

                elif action_input == 3:
                    list_renters()

                elif action_input == 4:
                    insert_apartment()

                elif action_input == 5:
                    get_recommendations()

                elif action_input == 6:
                    log_out()

                elif action_input == 7:
                    print('👋 Goodbye!')
                    quit()

                else:
                    print('❌ Invalid Option!')

            
# apartment_renter_managment()

def check_version():
    print(pd.__version__)

# check_version()

def max_rows():
    print(pd.options.display.max_rows)

# max_rows()

def create_dataframe():
    dataset = {
        'cars' : ['Tesla', 'Rivian', 'Lucid'],
        'passings' : [9,4,1]
    }

    my_dataset = pd.DataFrame(dataset)
    print(my_dataset)

# create_dataframe()

def create_series():
    nums = [1,5,8]
    series = pd.Series(nums, index=['num1', 'num2', 'num3'])
    print(series['num1'])

# create_series()

def dictionary_series():
    calories = {'day1':400, 'day2':390, 'day3':460}
    calorie_series = pd.Series(calories)
    print(calorie_series)

# dictionary_series()

def calories_dataframe():
    calories = {
        'calories':[400,390,460],
        'duration':[38,36,50]
    }
    calories_dataframe = pd.DataFrame(calories, index=['Day 1', 'Day 2', 'Day 3'])
    print(calories_dataframe)

# calories_dataframe()

def csv_dataframe():
    dataframe = pd.read_csv('data.csv')
    print(dataframe)

# csv_dataframe()

def csv_data():
    csv_data = pd.read_csv('data.csv')
    print(csv_data.to_html())


# csv_data()

def dictionary_dataframe():
    
    data = {
    "Duration":{
        "0":60,
        "1":60,
        "2":60,
        "3":45,
        "4":45,
        "5":60
    },
    "Pulse":{
        "0":110,
        "1":117,
        "2":103,
        "3":109,
        "4":117,
        "5":102
    },
    "Maxpulse":{
        "0":130,
        "1":145,
        "2":135,
        "3":175,
        "4":148,
        "5":127
    },
    "Calories":{
        "0":409,
        "1":479,
        "2":340,
        "3":282,
        "4":406,
        "5":300
    }
    }
    df = pd.DataFrame(data)
    print(df)

# dictionary_dataframe()

def drop_empty_cells():
    dataframe = pd.read_csv('data.csv')
    dataframe.dropna(inplace=True)
    print(dataframe)


# drop_empty_cells()

def fill_empty_cells():
    dataframe = pd.read_csv('data.csv')
    avg_calorie = dataframe['Calories'].mean()
    dataframe.fillna(avg_calorie, inplace=True)
    print(dataframe)

# fill_empty_cells()

def convert_format_of_date():
    dataframe = pd.read_csv('data.csv')
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='mixed')
    print(dataframe.to_string())

# convert_format_of_date()

def fix_wrong_data():
    data = pd.read_csv('data.csv')
    data.loc[7, 'Duration'] = 45
    print(data.to_string())

# fix_wrong_data()

def fix_all_wrong_data():
    data = pd.read_csv('data.csv')
    for i in data.index:
        if data.loc[i, 'Duration'] > 120:
            data.loc[i, 'Duration'] = 120
    
    print(data.to_string())

# fix_all_wrong_data()

def find_duplicates():
    data = pd.read_csv('data.csv')
    print(data.duplicated())

# find_duplicates()

def delete_duplicates():
    data = pd.read_csv('data.csv')
    data.drop_duplicates(inplace=True)
    print(data.to_string())

# delete_duplicates()

def correlation():
    data = pd.read_csv('data.csv')
    return data.corr()
    

# print(correlation())

def data_graphing():
    data = pd.read_csv('data.csv')

    # data.plot(kind='hist', x='Duration', y='Calories')
    data['Duration'].plot(kind='hist')

    mat.show()

# data_graphing()

data = pd.read_csv('data.csv')
# print(data.describe())

students_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eshan"],
    "Age": [14, 16, 15, 18, 13],
    "Grade": ["9th", "10th", "9th", "12th", "8th"]
})



def first_3_rows():
    return students_data.head(3)

# print(first_3_rows())

def name_column():
    return students_data['Name']

# print(name_column())

def older_than_15():
    older_students = students_data[students_data['Age'] > 15]
    return older_students

# print(older_than_15())

def binary_to_decimal():
    binary_num_input = input('Enter a number in binary: ')
    binary_nums = list(binary_num_input)

    result = 0

    for i in range(len(binary_nums)):
        if binary_nums[-(i+1)] == '1':
            result += 2**i

    return result

# print(binary_to_decimal())

class NumPy:
    def version():
        return np.__version__

    # print(version())


    def fruits_array():
        arr = np.array(['strawberry', 'blueberries', 'cherrries', 'dragonfruit'])
        return arr[3]

    # print(fruits_array())


    def int_and_float_array():
        nums = np.array([1,1.5,1.90,6,7])
        return nums[3]

    # print(int_and_float_array()


    def zero_dimension_array():
        arr = np.array(42)
        return arr

    # print(zero_dimension_array())



    def one_dimension_array():
        arr = np.array([1,2,3,4,5])
        return arr

        

    # print(one_dimension_array())


    def two_dimension_array():
        arr = np.array([1,2,3,4,5], [6,7,8,9,10])
        return arr

        
    # print(two_dimension_array())



    def three_dimension_array():
        arr = np.array([[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]])
        

    # print(three_dimension_array())


    def check_dimensions():
        arr0 = np.array(42)
        arr1 = np.array([1,2,3,4,5])
        arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
        arr3 = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]]])

        return np.ndim(arr0), np.ndim(arr1), np.ndim(arr2), np.ndim(arr3)

    # print(check_dimensions())

    def multi_dimension_array():
        arr = np.array([1,2,3,4,5], ndmin=5)
        return arr, arr.ndim

    # print(multi_dimension_array())

    def adding_elements_in_array():
        arr = np.array([1,2,3,4,5])
        return arr[0] + arr[1]

    # print(adding_elements_in_array())

    def access_two_d_elements():
        arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
        return arr[0,1]

    # print(access_two_d_elements())

    def access_3_d_elements():
        arr = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]]])
        return arr[1,0,3]

    # print(access_3_d_elements())

    def slicing_array():
        arr = np.array([1,2,3,4,5,6,7,8,9,10])
        return arr[1:8:2]

    # print(slicing_array())

    def dtype_of_array():
        arr = np.array([1,2,3,4,5])
        return arr.dtype

    # print(dtype_of_array())

    def dtype_of_str_array():
        arr = np.array(['strawberries', 'blueberries', 'dragonfruit'])
        return arr.dtype

    # print(dtype_of_str_array())

    def change_dtype_of_array():

        arr = np.array([1,2,3,4,5])


        newarr = arr.astype(dtype='f')

        return arr, newarr

    # print(change_dtype_of_array())



    def copy():
        arr = np.array([1,2,3,4,5,42])
        copy_of_array = arr.copy()
        arr[5] = 6
        return arr, copy_of_array, copy_of_array.base

    # print(copy())


    def view():
        arr = np.array([1,2,3,4,5,42])
        view_of_array = arr.view()
        arr[5] = 6
        return arr, view_of_array, view_of_array.base 

    # print(view())



    def reshape():
        arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
        newarr = arr.reshape(4,3)
        return newarr

    # print(reshape())


    def flatten_array():
        arr = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[2,4,6,8,10], [1,3,5,7,9]]])
        flattened_arr = arr.reshape(-1)
        return flattened_arr

    # print(flatten_array())

    def array_iteration():
        arr = np.array([1,2,3,4,5])
        for num in arr:
            print(num)

        
    # array_iteration()

    def two_dimension_array_iteration():
        arr = np.array([[1,2,3], [4,5,6]])
        for x in arr:
            for y in x:
                print(y)
            


    # two_dimension_array_iteration()

    def nditer():
        arr = np.array([[1,2,3], [4,5,6]])
        for x in np.nditer(arr):
            print(x)

    # nditer()

    def op_dtypes():
        arr = [[[1,2,3], [4,5,6]]]
        for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
            print(x)
        
    # op_dtypes()

    def ndenumerate():
        arr = np.array([[1,2,3], [4,5,6]])
        for idx, x in np.ndenumerate(arr):
            print(idx, x)

    # ndenumerate()

    def concatenate_arrays():
        arr1 = np.array([1,2,3])
        arr2 = np.array([4,5,6])

        concat_arrays = np.concatenate((arr1, arr2))

        return concat_arrays


    # print(concatenate_arrays())


    arr1 = np.array([[1,2,3], [4,5,6]])
    arr2 = np.array([[1,3,5], [2,4,6]])

    concat_arrays = np.concatenate((arr1, arr2), axis=1)

    # print(concat_arrays)

    def stack():
        arr1 = np.array([1,2,3])
        arr2 = np.array([4,5,6])

        return np.stack((arr1, arr2))

    # print(stack())


    def hstack():
        arr1 = np.array([1,2,3])
        arr2 = np.array([4,5,6])

        return np.hstack((arr1, arr2))

    # print(hstack())


    def vstack():
        arr1 = np.array([1,2,3])
        arr2 = np.array([4,5,6])

        return np.vstack((arr1, arr2))

    # print(vstack())

    def dstack():
        arr1 = np.array([1,2,3])
        arr2 = np.array([4,5,6])

        return np.dstack((arr1, arr2))


    # print(dstack())


    def array_split():
        arr = np.array([1,2,3,4,5,6])

        return np.array_split(arr, 2)


    # print(array_split())

    def two_d_array_split():
        arr = np.array([[1,2], [2,3], [4,5], [6,7], [8,9]])

        return np.array_split(arr, 3)


    # print(two_d_array_split())

    def hsplit():
        arr = np.array([[0,1], [2,3], [4,5], [6,7], [8,9]])

        return np.hsplit(arr, 2)


    # print(hsplit())

    def array_search():
        arr = np.array([1,8,2,2,8,5,3,2])
        x = np.where(arr == 2)

        return x


    # print(array_search())

    def searchsorted():
        arr =  np.array([1,3,4,5])
        x = np.searchsorted(arr, 2, side='left')

        return x


    # print(searchsorted())

    def multiple_searchsorted_values():
        arr = np.array([1,3,7,9])
        x = np.searchsorted(arr, [2, 6, 8], side='left')

        return x


    # print(multiple_searchsorted_values())

    def sort_by_value():
        arr = np.array([1,9,2,8,3,7,4,6,5])
        sort_array = np.sort(arr)

        return sort_array


    # print(sort_by_value())

    def sort_alphabetically():
        fruits_arr = np.array(['banana', 'cherry', 'apple'])
        sort_array = np.sort(fruits_arr)

        return sort_array


    # print(sort_alphabetically())

    def sort_by_boolean():
        boolean_arr = np.array([True, False, True, False])
        sort_array = np.sort(boolean_arr)

        return sort_array


    # print(sort_by_boolean())

    def sort_two_d_arrays():
        arr = np.array([[1,2,3], [4,5,6]])
        sort_array = np.sort(arr)

        return sort_array


    # print(sort_two_d_arrays())

    def filter_array():
        arr = np.array([0,1,2,3,4,5,6,7,8,9])
        filter_booleans = [True, False, True, False, True, False, True, False, True, False]
        newarr = arr[filter_booleans]

        return newarr


    # print(filter_array())

    def conditional_filter_array():
        arr = np.array([0,1,2,3,4,5,6,7,8,9])
        filter_booleans = []
        
        for element in arr:
            if element % 2 != 0:
                filter_booleans.append(True)
            else:
                filter_booleans.append(False)
        
        newarr = arr[filter_booleans]

        return newarr


    # print(conditional_filter_array())


    def filter_big_numbers():
        arr = np.array([1,2,3,4,5,6])
        big_nums = arr > 3
        newarr = arr[big_nums]
        return newarr


    # print(filter_big_numbers())


    def filter_even_numbers():
        arr = np.array([0,1,2,3,4,5,6,7,8,9])

        even_nums = arr % 2 == 0
        even_arr = arr[even_nums]

        return even_arr


    # print(filter_even_numbers())

    def copy_review():
        arr = np.array([1,2,3,4,5,6])
        arr_copy = arr.copy()
        arr[0] = 5

        return arr_copy


    # print(copy_review())

    def view_review():
        arr = np.array([1,2,3,4,5,6])
        arr_view = arr.view()
        arr[0] = 5

        return arr_view


    # print(view_review())

    def shape_review():
        arr = np.array([[1,2,3], [4,5,6]])
        return np.shape(arr)


    # print(shape_review())

    def graphing():
        x = np.array([0,6])
        y = np.array([1,0])
        mat.plot(y, marker='o')
        mat.show()

    # graphing()

    class ChatGPTPractice:
        def create_array():
            arr = np.array([10,20,30,40,50])
            
            return np.ndarray, arr.dtype
        
        def array_slice_and_index():
            arr = np.array([1,2,3,4,5,6,7])

            return arr[3], arr[-1], arr[1,5]
        
        def array_reshape():
            arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
            shape = arr.shape
            reshape = arr.reshape(3,4)

            return shape, reshape
        
        def join_split_arrays():
            arr1 = np.array([1,2,3])
            arr2 = np.array([4,5,6])
            newarr = np.concatenate((arr1, arr2))
            split_array = np.split(newarr, 3)

            return newarr, split_array
        

    practice_problems = ChatGPTPractice()


numpy = NumPy()





        




