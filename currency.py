def convertCurrency(amount, rate):
	return  amount*rate;

amount = 0;
rate = 0;

print("Enter the amount to be converted.......", end="");
while True:
    amount = input();
    if(amount.isnumeric()):
        amount = eval(amount);
        break;
    else:
        print("Enter a valid amount")
        
        
print("Enter the rate of conversion.......", end="");
while True:
    rate = input();
    if(rate.isnumeric()):
        rate = eval(rate);
        break;
    else:
        print("Enter a valid rate")
        
print("Expected value ", convertCurrency(amount, rate));