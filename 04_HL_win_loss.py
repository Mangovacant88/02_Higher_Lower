# HL component 5 - compares user guess with secret number

# to do
# set up number of guesses
# count # of guesses
# if user runs out of guesses, print 'you lose'
#if user guesses the secret number within the number of guesses print 'well done'

# HL componet 5
SECRET = 7
GUESSES_ALLOWED = 5

#initialise variables
already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))      # replace this with function call in due count

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again. "
              "You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    # if user has guesses left..
    if guesses_left >= 1:

        if guess < SECRET:
            print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

        elif guess > SECRET:
            print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
    else:
        if guess < SECRET:
            print("Too low!")
        elif guess > SECRET:
            print("Too high")

if guess == SECRET:
    if guesses_left == GUESSES_ALLOWED - 1:
        print("Amazing! You got it in one guess")
    else:
        print("Well done, you got it in {} guesses".format(len(already_guessed)))
    num_won += 1
else:
    print("Sorry - you lose this round as you have run out of guesses")










