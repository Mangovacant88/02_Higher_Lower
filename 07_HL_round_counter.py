# HL Component 7 - Generates desired number of rounds

rounds = int(input("How many rounds?"))  # Check with integer in due count
rounds_played = 0

while rounds_played < rounds:
    print("Round {}".format(rounds_played))
    rounds_played += 1

print("You have gotten to thr end of the game")