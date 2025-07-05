import random
options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
computer_choice = random.choice(options)
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
            print("You are out of tries!")
            break
except ValueError:
    print("Invalid response, please try again.")



