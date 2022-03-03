
def getData():
    listSize = int(input("How many names in the list: "))
    phoneList = []
    nameList = []
    for i in range(listSize):
        name = input("Name: ")
        phone = input("Phone: ")
        phoneList.append(phone)
        nameList.append(name)
    return phoneList, nameList


def getHighTemps(phoneList):
    number = input("Enter phone number to search for: ")
    numEqualList = []
    for i in range(len(phoneList)):
        if phoneList[i] == number:
            numEqualList.append(i)
    return numEqualList


def printResults(numEqualList, nameList):
    if (len(numEqualList) == 0):
        print("Phone number not found")
    else:
        for i in range(len(numEqualList)):
            x = numEqualList[i]
            print("Phone number belongs to ", nameList[x])
    return

# Main function
def main():
    phoneList, nameList = getData()
    numEqualList = getHighTemps(phoneList)
    printResults(numEqualList, nameList)

main()