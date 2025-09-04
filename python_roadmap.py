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


# print(stack.pop())
# print(stack.peek())
# print(stack.top())
# print(stack.is_empty())
# print(stack.push('Acai Berries'))
# print(fruits)

# nums = (x for x in range(100))
# print(next(nums))

nums = [1,2,3,4,5]
print(quit(nums))




              

 

        



        








