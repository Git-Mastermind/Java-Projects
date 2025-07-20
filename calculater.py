operation_choice = input('Do you want to add, subtract, multiply, divide, power, or log? ')
    if 
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

def logarithms(log_arg, base):
    log_ans = math.log(log_arg, base)
    return log_ans


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
    case 'log':
        print(logarithms(int(input('Enter a logarithms argument: ')), int(input('Enter a base: '))))

