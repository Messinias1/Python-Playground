
golfers = int(input("How many golfers are in the tournament? "))
golferScores = []
cutArr = []

for i in range(golfers):
    scores = int(input("Enter two-day score for golfer " + str(i + 1) + ": "))
    golferScores.append(scores)

cutOff = int(input("Enter the cut-off score: "))

for i in range(len(golferScores)):
    if(golferScores[i] < cutOff):
        cutArr.append(golferScores[i])

if(len(cutArr) == 0):
    print("No golfers made the cut")
else:
    golfersCut = (len(cutArr) / len(golferScores)) * 100
    print("The percent of golfers that made the cut is ", golfersCut, " %.")


