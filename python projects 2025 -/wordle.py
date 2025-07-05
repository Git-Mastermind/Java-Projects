while True:
        word = ["b","o","o","k","s"]
        options = [b]

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
        break







