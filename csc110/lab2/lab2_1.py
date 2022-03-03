
starRating = int(input("Enter star rating: "))
shares = int(input("Enter number of shares: "))
score = 0

if starRating == 1 or starRating == 2 and shares < 1000:
    score = (starRating * shares) * 2
elif starRating == 1 or starRating == 2 and shares >= 1000:
    score = (starRating * shares)
elif starRating == 3 or starRating == 4 and shares < 2500:
    score = (starRating * shares) * 3
elif starRating == 3 or starRating == 4 and shares >= 2500:
    score = (starRating * shares)
elif starRating == 5 and shares < 5000:
    score = (starRating * shares) * 4
else:
    score = starRating * shares

print("The score is: ", score)
