
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
attempts = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        print("You have " + str(attempts) + " attempts left, Good Luck!")
        guess = input("Enter guess: ")
        guess_count += 1
        attempts -= 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose :(")
else:
    print("You Win!, Congrats!")