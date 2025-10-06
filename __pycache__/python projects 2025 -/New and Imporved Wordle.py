import random


x = open('../100_five_letter_words.txt', 'r')
y = x.read()
word_list = y.split()
word = random.choice(word_list)
random_word_list = list(word)
output = []
int_checker = []


for x in range(6):
    message = input('Guess the word: ')
    if len(message) != 5:
        print('Geeeeeeeet out!!!!!')
        quit()
    elif len(message) == 5:
        message_character_split = list(message)
        for y in range(5):
            if message_character_split[y].isalpha():
                int_checker.append('1')
            else:
                int_checker.append('2')
        if '2' in int_checker:
            print('Geeeeeeeet out!!!!!')
            int_checker.clear()
            quit()
        else:
            for i in range(5):
                if random_word_list[i] in message:
                    if random_word_list[i] == message[i]:
                        output.append('💚')
                    else:
                        output.append('💛')
                else:
                    output.append('❤️')
            print(*output)
            output.clear()
print(f'You lost! The word was {word}! You suck')




















