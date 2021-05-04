from random import *


def roll_d6():
    num = randint(1,6)
    return num


final_score = 0

def player(x):
    all_turns = []
    for i in range(10):
        turn = []
        score = 0

        for i in range(x):
            turn.append(roll_d6())

        if 1 in turn:
            all_turns.append(0)
        else:
            for i in turn:
                score += i
            all_turns.append(score)
    return all_turns

def sum(player):
    final_score = 0
    all_turns = player
    for i in all_turns:
        final_score += i
    return final_score

for i in range(10):
    print(sum(player(4)))