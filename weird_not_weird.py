def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False



def is_between(number, starting_value, ending_value):
    if starting_value <= number <= ending_value:
        return True
    else:
        return False

input_number = int(input('Enter a number: '))

try:
    if 1 <= input_number <= 100:
        if is_odd(input_number):
            print('Weird')
        elif not is_odd(input_number) and is_between(input_number, 2, 5):
            print('Not Weird')
        elif not is_odd(input_number) and is_between(input_number, 6, 20):
            print('Weird')
        elif input_number > 20:
            print('Not Weird')
    else:
        print('Invalid Domain (1 <= number <= 100)')
except ValueError:
    print('Invalid Value (enter valu int 1<=number<=100)')

