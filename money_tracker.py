print('Your balance starts off with: 1')
balance = 1

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

def check_balance(balance):
    print(f'Your balance is: 💲{balance}')

while balance > 0:
    bank_selection = ''
    while bank_selection != 'q':
        bank_selection = input('(D)eposit, (W)ithdraw, or (C)heck Balance? (q to quit): ').lower()
        if bank_selection == 'd':
            amount = int(input('Deposit amount: '))   
            balance = deposit(balance, amount)
        elif bank_selection == 'w':
            amount = int(input('Withdraw amount: '))
            balance = withdraw(balance, amount)
        elif bank_selection == 'c':
            check_balance(balance)

    else:
        quit()

else:
    print('Your balance is less than zero!')