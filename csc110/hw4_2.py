# Carl Kakisis
# SumKDigits hw4_2
# Due Date: 2/28/22

# initializing sumKDigits
def sumKDigits(num, k):
    # initializing global variables
    sum = 0
    counter = 1
    # putting the digits of the integer in an array
    x = [int(a) for a in str(num)]

    # looping through the array of digits
    for i in x:
        if counter <= k:
            counter += 1
            sum += i
        if k > len(x):
            return 0
    return sum

# calling the main function
def main():
    print(sumKDigits(829383472934, 6))\

main()
