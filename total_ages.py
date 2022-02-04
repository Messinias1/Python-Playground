
def main():
    first_age = int(input('enter your age: '))
    second_age = int(input("enter your best friends age: "))
    total = sum(first_age,second_age)
    print('together you are', total, 'years old')


def sum(num1, num2):
    result = num1 + num2
    return result


main()