def say_hello():
    return print('hello')
say_hello()

nums = [1,2,3,4,5,6]

def pop_and_remove():
    popped_value = nums[-1]
    del nums[-1]
    return popped_value

print(nums)
print(pop_and_remove())
print(nums)