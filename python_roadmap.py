from collections import deque


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
raising_exceptions.safe_divide(2,0)







    









              

 

        



        








