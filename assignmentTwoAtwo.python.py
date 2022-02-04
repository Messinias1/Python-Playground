
# use a for loop with a range to distinguish months
# a while loop will be needed to check if snow < 0
# do not use an array, make first value largest
# then using an if statement to compare and swap if applicable.

jan_snowfall = float(input("Enter the total inches "
                           "of snowfall for January: "))
while jan_snowfall < 0:
    print("Please enter an amount of 0 or greater and try again...")
    jan_snowfall = float(input("Please enter the new amount of snowfall"
                               " for January: "))

feb_snowfall = float(input("Enter the total inches "
                           "of snowfall for February: "))
while feb_snowfall < 0:
    print("Please enter an amount of 0 or greater and try again...")
    feb_snowfall = float(input("Please enter the new amount of snowfall"
                               " for February: "))

march_snowfall = float(input("Enter the total inches "
                             "of snowfall for March: "))
while march_snowfall < 0:
    print("Please enter an amount of 0 or greater and try again...")
    march_snowfall = float(input("Please enter the new amount of snowfall"
                               " for March: "))

total_snowfall = jan_snowfall + feb_snowfall + march_snowfall
mean_snowfall = total_snowfall / 3

