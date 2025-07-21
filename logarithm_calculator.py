def logarithm_calculator(argument, base):
    answer = 0
    is_perfect_log = False

    while argument > 1:
        if argument % base == 0:
            argument = argument // base
            answer += 1

        else:
            print('Not perfect logarithm')
            is_perfect_log = True
            break

    if is_perfect_log == False:
        print(answer)
    
        
argument = int(input('Enter the logarithm argument: '))
base = int(input('Enter a base: '))

logarithm_calculator(argument, base)



