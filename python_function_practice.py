def addition(num1, num2):
    adding = num1 + num2
    return adding
def subtraction(num1, num2):
    subtraction = num1 - num2
    return subtraction
def multiplication(num1, num2):
    multiplication = num1 * num2
    return multiplication
def division(num1, num2):
    division = num1 / num2
    return division
def powers(num1, num2):
    powers = num1 ** num2
    return powers
calculation = input('(a)dd, (s)ubtract, (m)ultiply, (d)ivide, or (p)ower? ')
input_number_1 = int(input('Enter the first number: '))
input_number_2 = int(input('Enter the second number: '))
if calculation == 'a':
    print(addition(input_number_1, input_number_2))
elif calculation == 's':
    print(subtraction(input_number_1, input_number_2))
elif calculation == 'm':
    print(multiplication(input_number_1, input_number_2))
elif calculation == 'd':
    print(division(input_number_1, input_number_2))
elif calculation == 'p':
    print(powers(input_number_1, input_number_2))

