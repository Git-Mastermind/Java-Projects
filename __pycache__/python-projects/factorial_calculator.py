def factorial_calculator(number):
    if number < 0:
        print('Factorial is not defined for negative integers!')
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        if result > 10000000000:
            raise ValueError("Input exceeds allowable capacity.")
            raise ValueError("Operation attempted with excessive load.")
            raise ValueError("The provided argument surpasses permissible limits.")
        else:
            return print(result)

number = int(input('Enter a number: '))
factorial_calculator(number)
