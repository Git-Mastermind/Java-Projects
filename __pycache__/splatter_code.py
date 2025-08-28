#  cities = ['seattle', 'bentonville', 'new york', 'madison', 'manhatten']

# # city_names = ''
# # loop_counter = -1
# # for city in cities:
# #     loop_counter += 1
# #     if loop_counter == 0:
# #         city_names = city
# #     elif 1 <= loop_counter < len(cities) - 1:
# #         city_names = city_names + ', ' + city
# #     else:
# #         city_names = city_names + ' and ' + city

# # print(city_names)
# import tkinter as tk
    
# def first_letter_of_words():
#     input_sentence = input('Enter a sentence (each word space seperated): ')
#     each_word = input_sentence.split()
#     first_letter_of_word = []
#     for i in range(len(each_word)):
#         first_letter_of_word.append(each_word[i][0])
#     print(*first_letter_of_word)


# def first_letter_of_each_word():
#     input_sentence = input('Enter a sentence (seperated by space) ')
#     characters = list(input_sentence)
#     result = []
#     for i in range(len(characters)):
#         if i == 0:
#             result.append(characters[i])
#         elif characters[i] == ' ':
#             result.append(characters[i + 1])
#     print(*result)

# # first_letter_of_each_word()