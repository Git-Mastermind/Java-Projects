user_input = input('Enter a series of numbers seperated with spaces: ')
numbers = user_input.split()
# Each number is now a token with type str
number_list = list(map(int, numbers))
# Turning each token into type int
even_number_list = []
# Empty list for later
for i in range(0, len(number_list)):
    if number_list[i] % 2 == 0:
        even_number_list.append(number_list[i])
        # If the remainder of token[i] is 0, it is even and therefore should be appended into a different list

if len(even_number_list) == 0:
    print('There are no odd numbers in this list!')
    # If there are only odd numbers in this list, it will return no values
print(*even_number_list)
# Print the list containing even numbers without the square brackets