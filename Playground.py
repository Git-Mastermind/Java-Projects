from functools import reduce

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

multiplier = lambda n : (lambda x : x*n)

def square_numbers():
    nums = [1,2,3,4]
    square_nums = list(map(lambda num:num**2, nums))
    print(square_nums)

# square_numbers()

def evens_list():
    nums = [10,15,20,25]
    keep_evens = list(filter(lambda num : num % 2 == 0, nums))
    print(keep_evens)

# evens_list()

def reduce_list_to_products():
    nums = [1,2,3,4,5]
    full_product = reduce(lambda x,y:x*y,nums)
    print(full_product)

# reduce_list_to_products()

def cube_every_number():
    nums = [1,2,3,4,5]
    cube_each_num = list(map(lambda num:num**3, nums))
    print(cube_each_num)

# cube_every_number()

def filter_greator_than_10():
    nums = [5,12,19,21,30,3]
    filtered_nums = list(filter(lambda num : num > 10, nums))
    print(filtered_nums)

# filter_greator_than_10()

def sum_of_evens():
    nums = [2,4,6,8,10]
    sum_of_evens = reduce(lambda x,y:x+y,nums)
    print(sum_of_evens)

# sum_of_evens()

def multi_practice():
    fruits = ["apple", "banana", "pear", "kiwi", "strawberry"]
    lengths = list(map(lambda fruit : len(fruit),  fruits))
    
    keep_long_words = list(filter(lambda fruit : len(fruit) > 4, fruits))

    longest_word = reduce(lambda x, y : x if len(x) > len(y) else y, keep_long_words)

    print(lengths)
    print(keep_long_words)
    print(longest_word)

multi_practice()