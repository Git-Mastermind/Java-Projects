operation_choice = input('Do you want to add, subtract, multiply, divide or power? ')
numb1 = int(input('Enter the first number: '))
numb2 = int(input('Enter the second number: '))
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2


match operation_choice:
    case 'add':
        print(add(numb1, numb2))
    case 'subtract':
        print(subtract(numb1, numb2))
    case 'multiply':
        print(multiply(numb1, numb2))
    case 'divide':
        print(divide(numb1, numb2))
    case 'power':
        print(power(numb1, numb2))

