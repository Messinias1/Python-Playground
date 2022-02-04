
toyCount = int(input("How many toys are in the catalog? "))

i = 1
price = float(input("Enter toy price $"))
while i < toyCount:
    price += float(input("Enter toy price $"))
    i += 1

averagePrice = price / toyCount
print("The average price of toys in the catalog is : $ ", round(averagePrice, 2))
