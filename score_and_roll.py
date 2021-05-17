from main import roll_d6, sum



def player(x, y):
    all_turns = []
    for i in range(10):
        turn = []
        score = 0

        while True:
            turn.append(roll_d6())
            if 1 in turn:
                break

            if sum(turn) >= x or len(turn) == y:
                break

        if 1 in turn:
            all_turns.append(0)
        else:
            for i in turn:
                score += i
            all_turns.append(score)
    return all_turns

def avg(x, y):
    all_games = []
    all_games_score = 0
    for i in range(1000000):
        all_games.append(sum(player(x, y)))

    for game_score in all_games:
        all_games_score += game_score
        avg = all_games_score / len(all_games)
    return avg




# adding stricter range of aimed scores
def scores_strict(x, y, z, q):
    for i in range(x,y+1):
        for j in range(z,q+1):
            print(f"Aimed score/turn {i}, no more than {j} rolls, average score: {avg(i, j)}")


scores_strict(21,21,8,8)
scores_strict(21,21,9,9)
scores_strict(21,21,9,9)