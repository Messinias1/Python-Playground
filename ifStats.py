
isMale = True
isTall = True

if isMale and isTall:
    print("You are a tall male")
elif isMale and not(isTall):
    print("You are a short male")
elif not(isMale) and isTall:
    print("Not male but tall")
else:
    print("Not male or not tall")