number_list = []
for i in range(0,100):
    number_list.append(i)
for i in range(0,100):
    if number_list[i] % 3 == 0 and number_list[i] % 5 ==0:
        number_list[i] = 'FizzBuzz'
    elif number_list[i] % 3 == 0:
        number_list[i] = 'Fizz'
    elif number_list[i] % 5 == 0:
        number_list[i] = 'Buzz'
print(*number_list)