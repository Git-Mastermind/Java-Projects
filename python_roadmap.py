from collections import deque

from functools import reduce


fruits = ['strawberries', 'blueberries', 'cherries', 'grapes', 'blackberries', 'raspberries']

class Stacks:
    def pop(self):
        if len(fruits) == 0:
            print('List is empty 😅')
        else:
            popped_value = fruits[-1]
            del fruits[-1]
            return popped_value
        
        
    def peek(self):
        if len(fruits) == 0:
            print('List is empty 😅')
        else:
            return fruits[-1]
        
        
    def top(self):
        if len(fruits) == 0:
            print('List is empty 😅')
        else:
            return fruits[-1]
        

    def push(self, item):
        fruits.append(item)
        print('✅ Successfully pushed item!')


    def is_empty(self):
        if len(fruits) == 0:
            return True
        else:
            return False
        
stack = Stacks()


class Gen_Exp:

    def odd_squares():
        squares = (num**2 for num in range(20) if num % 2 != 0)
        for num in squares:
            print(num)



    def filter_short_words():
        words = ['cat', 'elephant', 'dog']
        filter_short_words = (word for word in words if len(word) < 5)
        for word in filter_short_words:
            print(word)


    def even_squares():
        squares = (num**2 for num in range(20) if num % 2 == 0)
        for num in squares:
            print(num)


    def first_letter_of_words():
        fruits = ['strawberries', 'cherries', 'blueberries']
        first_letter = [word[0] for word in fruits]
        for word in first_letter:
            print(word)


    def sort_by_7():
        filter_nums = (num for num in range(50) if num % 7 == 0)
        for num in filter_nums:
            print(num)


    def short_words_to_uppercase():
        words = ['hi', 'elephant', 'dog', 'python']
        short_words_to_uppercase = (word.upper() for word in words if len(word) < 6)
        for word in short_words_to_uppercase:
            print(word)


    def square_digits():
        number = '245'
        square_digits = (int(digit[0])**2 for digit in number)
        for digit in square_digits:
            print(digit)


    def reverse_each_word():
        words = ['cat', 'dog', 'bird']
        reverse_words = (word[::-1] for word in words)
        for word in reverse_words:
            print(word)


gen_exp = Gen_Exp()

class RaisingExceptions:
    def check_positive(self, num):
        if num < 0:
            raise ValueError('❌ Number cannot be negative!')
        else:
            print('✅ Number is positive')
    
    def safe_divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError('Cannot divide by zero!')
        else:
            return num1 / num2
    
    def get_element(self, list, index):
        if index > len(fruits):
            raise IndexError('Invalid Index!')
        else:
            return list[index]    

raising_exceptions = RaisingExceptions()


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

# multi_practice()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def describe(self):
        return f'{self.title} by {self.author}'

book = Book('The Land of Stories', 'Chris Colfer')

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def is_passing(self):
        if self.grade >= 60:
            return 'True'
        else:
            return 'False'

student = Student('Eshan', 99)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        balance = self.balance + amount
        self.balance = balance
        return f'✅ Deposit Successful! Your balance is now {balance}'
    
    def withdraw(self, amount):
        balance = self.balance - amount
        self.balace = balance
        return f'✅ Withdraw Successful! Your balance is now {balance}'

bank_account = BankAccount('Eshan', 309.5)
while True:
    choice = input('(D)eposit or (W)ithdraw: ').lower()
    if choice == 'd':
        amount = float(input('Amount: '))
        print(bank_account.deposit(amount))
    else:
        amount = float(input('Amount: '))
        print(bank_account.withdraw(amount))
    











    









              

 

        



        








