import random

# **** Main Routine *****

# Initialise variables
SECRET = 7
GUESSES_ALLOWED = 4
rounds = 3

num_won = 0
rounds_played = 0

# list holds # of guesses used in each game
game_stats = []

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    while guess != SECRET and guesses_left >= 1:
        guess = int(input("Guess: "))
        guesses_left -= 1

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
                num_won += 1
            else:
                print("Well done, you got it in {} guesses".format(GUESSES_ALLOWED - guesses_left))
                num_won += 1
        else:
            print("Sorry - you lose this round as you have run out of guesses")

    game_stats.append(GUESSES_ALLOWED - guesses_left)

    print("Won : {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

# print game outcomes...
print("*** Score for Each Round...***")
list_count = 1
for item in game_stats:

    # indicates if games has been won or lost
    if item > GUESSES_ALLOWED:
        status = "lost, ran out of guesses"
    else:
        status = "won"

    print("Round {}: {})".format(list_count, item))
    list_count += 1

# Calculate statistics
game_stats.sort()
best = game_stats[0]
worst = game_stats[-1]
average = sum(game_stats)/len(game_stats)

print()
print("*** Summary Statistics ***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))
