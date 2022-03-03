
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))

c = a
i = 1
while i < b:
    c *= a
    i += 1

print(a, " ** ", b, " = ", c)