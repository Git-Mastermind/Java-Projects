message = input('Enter a couple of numbers seperated by a space: ')
number_strings = message.split()
numbers = []
for num in number_strings:
    numbers.append(int(num))
max_number = numbers[0]
for i in range(1, len(numbers)):
    if max_number < numbers[i]:
        max_number = numbers[i]
print(f'The maximum number is: {max_number}')
