
total = 0
maximum = 0
count = 1

for month in range(3):
    snowfall = float(input("Enter snowfall for month "
                           + str(count) + ": "))
    while snowfall <= 0:
        print("Enter snowfall greater than 0")
        snowfall = float(input("Enter snowfall for month "
                               + str(count) + ": "))
    total += snowfall
    if snowfall > maximum:
        maximum = snowfall
    count += 1

mean = total / 3

print("")
print("The maximum snowfall during the three month period is: ")
print(format(maximum, '.2f'))
print("")
print("The total snowfall over the three month period is: ")
print(format(total, '.2f'))
print("")
print("The average snowfall over the three month period is: ")
print(format(mean, '.2f'))
print("")

if total > 24:
    difference = total - 24
    print("The three month snowfall record has been broken by ",
          format(difference, '.2f'), " inches with a new total of: ",
          format(total, '.2f'))
else:
    print("Snowfall was average for the three month period")