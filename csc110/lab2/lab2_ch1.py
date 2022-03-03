
numLimit = int(input("Enter the highest number to consider: "))

total = 0

for i in range(numLimit):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print("The sum of all multiples of 3 and 5 below ", numLimit, " is: ", total)