
sale = float(input("Enter amount of sale$ "))

if(sale > 600):
    finalSale = sale * .7;
    print("The final sale amount is $", "{:,.2f}".format(finalSale))
elif(sale > 300 and sale <= 600):
    finalSale = sale * .8;
    print("The final sale amount is $", "{:,.2f}".format(finalSale))
elif (sale > 100 and sale <= 300):
    finalSale = sale * .9;
    print("The final sale amount is $", "{:,.2f}".format(finalSale))
else:
    finalSale = sale * .95;
    print("The final sale amount is $", "{:,.2f}".format(finalSale))