import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {
    ROCK:'🪨',
    SCISSORS:'✂️',
    PAPER:'📜'
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



