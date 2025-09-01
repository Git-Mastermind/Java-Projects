from collections import deque


fruits = ['strawberries', 'blueberries', 'cherries', 'grapes', 'blackberries', 'raspberries']

class Stacks:
    def pop(self):
        if len(fruits) == 0:
            print('List is empty 😅')
        else:
            return fruits[-1]
        
        
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


    def is_empty(self):
        if len(fruits) == 0:
            return True
        else:
            return False
        
stack = Stacks()

stack.pop()

              

 

        



        








