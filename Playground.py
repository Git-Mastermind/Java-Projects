def lambda_calculator():
    add = lambda num1, num2 : num1 + num2
    subtract = lambda num1, num2 : num1 - num2
    multiply = lambda num1, num2 : num1 * num2
    divide = lambda num1, num2 : num1/num2

    print(add(5,2))
    print(subtract(5,2))
    print(multiply(5,2))
    print(divide(5,2))

# lambda_calculator()

def lamdba_cubed():
    cube_number = lambda num : num**3
    print(cube_number(3))

# lamdba_cubed()

def sorted_numbers():
    nums = [(1,5), (3,2), (4,2)]
    sorted_nums = sorted(nums, key=lambda pair:pair[1])
    print(sorted_nums)

# sorted_numbers()

def palindrome_checker():
    word = input('Enter a word: ')
    palindrome_check = lambda word : True if word[::-1] == word else False
    print(palindrome_check(word))

# palindrome_checker()

def even_or_odd():
    num = int(input('Enter a number: '))
    even_or_odd = lambda num : 'Even' if num % 2 == 0 else 'Odd'
    print(even_or_odd(num))

# even_or_odd()


fruits = ['strawberries', 'blueberries', 'cherries', 'grapes', 'blackberries', 'raspberries']
print(sorted(fruits, key=lambda pair : len(pair)))