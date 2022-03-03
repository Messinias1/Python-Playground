
golfers = int(input("How many golfers are in the tournament? "))
golferArr = []
minimum = 1000
tournamentLeader = ""

for i in range(golfers):
    names = input("Enter name of golfer " + str(i + 1) + ": ")
    golferArr.append(names)
    scores = int(input("Enter score for golfer " + str(i + 1) + ": "))
    golferArr.append(scores)

i = 1
while i < len(golferArr):
    if(golferArr[i] < minimum):
        minimum = golferArr[i]
        tournamentLeader = golferArr[i - 1]
    i = i + 2

print("The current leader of the tournament is ", tournamentLeader, " with a score of ", minimum)





