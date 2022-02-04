
# Carl Kakisis
# 11/24/20
# COMI 1150-600

import random


def main():
    print("The sum of the random numbers is:", gen_rand_nums()[0])
    print("There were", gen_rand_nums()[1], "even numbers")
    print("There were", gen_rand_nums()[2], "odd numbers")


def gen_rand_nums():
    total = 0
    pos_num = 0
    neg_num = 0
    for count in range(50):
        num = random.randint(1, 100)
        total += num
        if num % 2 == 0:
            pos_num += 1
        else:
            neg_num += 1
    return total, pos_num, neg_num


main()
