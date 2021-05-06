from random import *

# rolling a d6 dice
def roll_d6():
    num = randint(1,6)
    return num

def player(x):
    all_turns = []
    for i in range(10):
        turn = []
        score = 0

        while True:
            turn.append(roll_d6())
            if 1 in turn:
                break

            if sum(turn) >= x:
                break

        if 1 in turn:
            all_turns.append(0)
        else:
            for i in turn:
                score += i
            all_turns.append(score)
    return all_turns

print(player(42))