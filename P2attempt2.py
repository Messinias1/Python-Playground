# Carl Kakisis
# 11/3/20
# COMI-1150-600:Programming Concepts

snowfallList = []

janSnowfall = float(input("Enter the total inches of snowfall for January: "))
snowfallList.append(janSnowfall)
febSnowfall = float(input("Enter the total inches of snowfall for February: "))
snowfallList.append(febSnowfall)
marSnowfall = float(input("Enter the total inches of snowfall for March: "))
snowfallList.append(marSnowfall)

print("")

totalSnowfall = 0

for i in snowfallList:
    totalSnowfall += i
    meanSnowfall = totalSnowfall / 3

if janSnowfall <= 0 or febSnowfall <= 0 or marSnowfall <= 0:
    print("Please enter an amount of snowfall for each month greater than 0 and try again..")
elif totalSnowfall > 24:
    difference = totalSnowfall - 24

    print("Maximum number of snowfall during 3 month period: ", max(snowfallList))
    print("Average amount of snowfall during 3 month period: ", format(meanSnowfall, '.2f'))
    print("Total snowfall during 3 month period: ", format(totalSnowfall, '.2f'))
    print("\nThe previous snowfall record of 24 inches from January through March has been broken with a new "
          "record by ", format(difference, '.2f'), " inches \nand a total of: ", format(totalSnowfall, '.2f'))
else:
    print("Maximum number of snowfall during 3 month period: ", max(snowfallList))
    print("Average amount of snowfall during 3 month period: ", format(meanSnowfall, '.2f'))
    print("Total snowfall during 3 month period: ", format(totalSnowfall, '.2f'))
    print("\nThe snowfall accumulation from January through March has been average")
