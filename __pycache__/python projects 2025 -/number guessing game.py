import random
try:
    number = random.randint(1, 20)
    previous_guesses = []
    user_input = int(input("Guess a number between 1 and 20: "))
    while user_input != number:
        if user_input in previous_guesses:
            print("You have already guessed that number!")
            user_input = int(input("Guess a number between 1 and 20: "))
        if user_input == number:
            print("Congratulations, you guessed it!")
        elif user_input > number:
            print("Too high!")
            previous_guesses.append(user_input)
            user_input = int(input("Guess a number between 1 and 20: "))
        elif user_input < number:
            print("Too low!")
            user_input = int(input("Guess a number between 1 and 20: "))
            previous_guesses.append(user_input)
except ValueError:
    print("You are a monkey!")