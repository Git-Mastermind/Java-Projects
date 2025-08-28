def decimal_to_binary(number):
    binary_answer = []
    if number == 0:
        print(0)
    else:
        while number > 0:
            binary_digit = number % 2
            binary_answer.append(binary_digit)
            number = number // 2

        print(*binary_answer[::-1])

decimal_to_binary(int(input('Enter a number: ')))