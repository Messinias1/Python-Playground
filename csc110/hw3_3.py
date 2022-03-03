
golfers = int(input("How many golf scores have you collected? "))
golferArr = []
kArr = []

for i in range(golfers):
    scores = int(input("Enter score: "))
    golferArr.append(scores)

kScore = int(input("Enter sample rate (k): "))

i = 0
while i < len(golferArr):
    kArr.append(golferArr[i])
    i = i + kScore

print("The sampled scores are:")
print(kArr)





