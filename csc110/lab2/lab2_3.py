
even = 0
odd = 0

num = int(input("Enter integer: "))

if num % 2 == 0:
    even += 1
else:
    odd += 1


i = 1
while i < 10:
    num = int(input("Enter integer: "))
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print("There are ", even, " even numbers in the list")
print("There are ", odd, " odd numbers in the list")