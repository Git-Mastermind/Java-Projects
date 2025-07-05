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






