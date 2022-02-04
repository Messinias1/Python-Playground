
# Carl Kakisis
# 11/24/20
# COMI 1150-600

# importing random to access random numbers
import random


def main():
    # declaring total, even and odd number variables to 0
    total = 0
    even_num = 0
    odd_num = 0
    # iterating 50 times for 50 random numbers
    for count in range(50):
        # declaring num variable to a random number between 1 and 100
        num = random.randint(1, 100)
        # adding each number to total
        total += num
        # bringing in the pos_or_neg function
        # if num is even, even_num count increases by 1
        # otherwise it is false, odd_num count increases by 1
        if pos_or_neg(num):
            even_num += 1
        else:
            odd_num += 1
    # printing the final results for total, even_num and odd_num
    print("The sum of the random numbers is:", total)
    print("There were", even_num, "even numbers")
    print("There were", odd_num, "odd numbers")

# This function will determine if a number is odd or even
# using modulus 2 and if so, the number is even and setting status to true
# otherwise the number is odd, status = false
# returning the value of status
def pos_or_neg(num):
    if num % 2 == 0:
        status = True
    else:
        status = False
    return status

# calling the main function
main()