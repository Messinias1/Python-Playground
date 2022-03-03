# Carl Kakisis
# allSumKDigits hw4_3
# Due Date: 2/28/22

# initializing allSumKDigits
def allSumKDigits(num):
    # initializing global variables
    sumArr = []
    sum = 0
    # putting the digits of the integer in an array
    x = [int(a) for a in str(num)]
    # setting bounds of next loop to sum
    counter = 0
    k = 1

    # looping through the array of digits and adding sum up
    # to the bound of k into sumArr
    for i in x:
        if counter < k and k <= len(x):
            sum += i
            sumArr.append(sum)
            counter += 1
            k += 1

    return sumArr

# calling the main function
def main():
    print(allSumKDigits(12345))
