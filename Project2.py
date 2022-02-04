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

totalSnowfall = janSnowfall + febSnowfall + marSnowfall
meanSnowfall = totalSnowfall / 3

if janSnowfall <= 0 or febSnowfall <= 0 or marSnowfall <= 0:
    print("Please enter an amount of snowfall for each month greater than 0 and try again..")
else:
    print("Maximum number of snowfall through 3 month period: ", max(snowfallList))
    print("Average amount of snowfall during 3 month period: ", meanSnowfall)
    print("Total snowfall during 3 month period: ", totalSnowfall)

if totalSnowfall > 24:
    print("The previous snowfall record of 24 inches from January through March has been broken with a new record of: ",
          totalSnowfall)
else:
    print("The snowfall accumulation from January through March has been average")
