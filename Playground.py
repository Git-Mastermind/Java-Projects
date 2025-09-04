def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError('Cannot divide by zero!')
    else:
        return num1/num2
    

print(int(division(2, 2)))