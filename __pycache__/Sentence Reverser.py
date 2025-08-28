message = input('Enter a sentence: ')
split = message.split()
number_of_words = len(split) + 1
for i in range(1, number_of_words):
     print(split[-i])


# list = [1,2,3,4,5,6]
# print(list[-2])
