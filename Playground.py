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

def second_index():
    nums = [(1,5), (3,2), (4,2)]
    sorted_nums = sorted(nums, key=lambda pair:pair[1])
    print(sorted_nums())

def palindrome_checker():
    word = input('Enter a word: ')
    palindrome_check = lambda word : True if word[::-1] == word else False
    print(palindrome_check(word))

palindrome_checker()