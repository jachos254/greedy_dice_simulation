from random import *

# rolling a d6 dice
def roll_d6():
    num = randint(1,6)
    return num



#full game of one player, x for number of planning rolls per one turn
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

#final score of one player
def sum(player):
    final_score = 0
    all_turns = player
    for i in all_turns:
        final_score += i
    return final_score




# average of games, x for number of planning rolls
def avg(x):
    all_games = []
    all_games_score = 0
    for i in range(1000):
        all_games.append(sum(player(x)))

    for game_score in all_games:
        all_games_score += game_score
        avg = all_games_score / len(all_games)
    return avg

# adding range of planned rolls
def rolls(i):
    for i in range(1,i+1):
        print(f"Rolls:{i}, average score: {avg(i)}")


rolls(10)