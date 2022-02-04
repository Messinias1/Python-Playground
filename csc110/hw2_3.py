min = 1000
max = 0
i = 1

for month in range(12):
    rainfall = float(input("Rainfall for month " + str(i) + ":"))

    if rainfall > max:
        max = rainfall

    if rainfall < min:
        min = rainfall
    i += 1

print("The highest monthly rainfall was ", max, " inches.")
print("The lowest monthly rainfall was ", min, " inches.")

