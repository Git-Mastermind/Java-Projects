def say_hello(*args):
    for name in args: 
        print(f'Hello {name}!')

def print_scores(**kwargs):
    for subject, score in kwargs.items():
        print(f'{subject}: {score}%')

def student_info(*args, **kwargs):
    print(f'Name: {args}')
    print(f'Scores: {kwargs}%')

def build_sandwich(*args, **kwargs):
    print(f'Sandwich ingreidiants: {args}')
    print(f'Extra Toppings: {kwargs}')

def print_scores_2(**kwargs):
    for subject, score in kwargs.items():
        print(f'{subject}: {score}')





