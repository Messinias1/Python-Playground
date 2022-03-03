# Carl Kakisis
# allSumKDigits hw4_1
# Due Date: 2/28/22

# asking user input for amount of toys in catalog and stroring their names, prices and sales in arrays
def getToys():
    catalogNumber = int(input("How many toys are in your catalog? "))

    toyNameArr = []
    toyPricesArr = []
    toysSoldArr = []

    for i in range(catalogNumber):
        toyName = input("Enter toy name: ")
        toyPrices = float(input("Enter toy price: "))
        toysSold = int(input("Enter number sold: "))

        toyNameArr.append(toyName)
        toyPricesArr.append(toyPrices)
        toysSoldArr.append(toysSold)

    return toyNameArr, toyPricesArr, toysSoldArr

# asking user for toy to search for, checking to see if input is equal to a value in toy names list
# setting the index equal to the position of the name
def searchToy(toyNameArr):
    toy = input("Enter a toy to find the price of: ")
    toyEqualList = []
    foundIndex = 0
    for i in range(len(toyNameArr)):
        if toyNameArr[i] == toy:
            foundIndex = i
            toyEqualList.append(i)
    return toyEqualList, foundIndex

def soldMore(toyNameArr, numSold, index):
    return

# printing results if no toy in catalog stating it, otherwise looping through the user entered toy list
# printing out toy and price seeing which toys have sold more and printing the ones that did to the console
# if not printing that no toys sold more
def printResults(toyEqualList, nameList, toyNameArr, index, toysSoldArr):
    soldMoreArr = []
    if (len(toyEqualList) == 0):
        print("The toy name you entered is not in our catalog.")
    else:
        for i in range(len(toyEqualList)):
            x = toyEqualList[i]
            print("The price of ", toyNameArr[index], " is $ ", nameList[x])
    threshold = 0
    for i in range(len(toysSoldArr)):
        threshold = toysSoldArr[index]
        if toysSoldArr[i] > threshold:
            soldMoreArr.append(toyNameArr[i])

    if(len(soldMoreArr) == 0):
        print("No toys have sold more than the ", toyNameArr[index])
    else:
        print("The toys that have more sold than the ", toyNameArr[index], " are: ")
        for j in range(len(soldMoreArr)):
            print(soldMoreArr[j])
    return

# Main function
def main():
    toyNameArr, toyPricesArr, toysSoldArr = getToys()
    toyEqualList, index = searchToy(toyNameArr)
    printResults(toyEqualList, toyPricesArr, toyNameArr, index, toysSoldArr)


