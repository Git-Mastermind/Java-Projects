from collections import deque




class Stacks:
    def __init__(self):
        self.stack = ['strawberries', 'blueberries', 'cherries', 'grapes', 'blackberries', 'raspberries']
    def pop(self):
        if len(self.stack) == 0:
            print('List is empty 😅')
        else:
            popped_index = self.stack[-1]
            del self.stack[-1]
            return popped_index
        
        
    def peek(self):
        if len(self.stack) == 0:
            print('List is empty 😅')
        else:
            return self.stack[-1]
        
        
    def top(self):
        if len(self.stack) == 0:
            print('List is empty 😅')
        else:
            return self.stack[-1]
        

    def push(self, item):
        self.stack.append(item)


    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
stack = Stacks()

stack.pop()

              

 

        



        








