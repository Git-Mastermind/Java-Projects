def logarithm_calculator(log_arg, base):
    log_ans = 0
    if_break = False
    while log_arg > 1:
        if log_arg % base == 0:
            log_arg = log_arg // base
            log_ans += 1
        else:
            print('Not perfect logarithm')
            if_break = True
            break
    if if_break == False:
        print(log_ans)
    
        

        



logarithm_calculator(int(input('Enter the logarithm argument: ')), int(input('Enter a base: ')))

