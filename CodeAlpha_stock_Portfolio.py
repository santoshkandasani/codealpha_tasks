
stock_prices={"AMAZON":100 ,"TESLA":120,"GOOGLE":130,"MICROSOFT":105,"ORACLE":90}

portfolio={}

while True:

    stock=input("Enter the name of stock (or 'done' to finish) ")
    stock=stock.upper()
    if stock == "DONE":
      break

    if stock in stock_prices :
       quantity=int(input(f"Enter number of stocks of {stock}: "))
       portfolio[stock]=quantity

    else:
       print("Stock not found in the list ")
    
value=0
print("-------Summary--------")
for stock,quantity in portfolio.items() :
   value += stock_prices[stock] *quantity
print("The total investment is :",value)