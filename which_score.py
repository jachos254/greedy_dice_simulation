from main import roll_d6, sum



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

def avg(x):
    all_games = []
    all_games_score = 0
    for i in range(10000):
        all_games.append(sum(player(x)))

    for game_score in all_games:
        all_games_score += game_score
        avg = all_games_score / len(all_games)
    return avg


# adding range of aimed scores
def scores(i):
    for i in range(1,i+1):
        print(f"Aimed score/turn: {i}, average score: {avg(i)}")

# adding stricter range of aimed scores
def scores_strict(x, y):
    for i in range(x,y+1):
        print(f"Aimed score/turn: {i}, average score: {avg(i)}")
