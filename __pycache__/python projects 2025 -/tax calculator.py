user_price = float(input("What was the price of your items?: "))
user_taxes = float(input("What is the sales tax for your area?: "))
user_tax = (user_price * user_taxes)/100 + user_price
print(f"Your total for today is ${round(user_tax,2)}!")