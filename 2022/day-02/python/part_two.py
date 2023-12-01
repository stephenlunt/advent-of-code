strategy = []

def main():
    read_file()

    total_score = 0
    for game in strategy:
        outcome = get_game_outcome(game)
        move = decide_move(game, outcome)
        score = score_game(outcome, move)
        total_score += score

    print(f"The total score is: {total_score}")


def read_file():
    with open("./day-02/input.txt") as f:
        for row in f:
            game = row.rstrip("\n").split(" ")
            strategy.append(game)


def get_game_outcome(game: list) -> int:
    """
    Returns -1 if we should lose the game, 0 if we should draw, and 1 if we should win.
    """
    match game[1]:
        case "X":
            return -1
        case "Y":
            return 0
        case "Z":
            return 1


def decide_move(game: list, outcome: int) -> str:
    """
    Returns the move to take as:
    'A' = player rock
    'B' = play paper
    'C' = play scissors
    """
    opponents_move = game[0]

    # Return a move to win the game
    if outcome == 1:
        match opponents_move:
            case "A":
                return "B"
            case "B":
                return "C"
            case "C":
                return "A"

    # Return a move to lose the game
    if outcome == -1:
        match opponents_move:
            case "A":
                return "C"
            case "B":
                return "A"
            case "C":
                return "B"

    # To draw, we match the opponents move
    if outcome == 0:
        return opponents_move


def score_game(outcome: int, move: str) -> int:
    # Score outcome
    if outcome == 1:
        game_score = 6
    elif outcome == 0:
        game_score = 3
    else:
        game_score = 0

    # Score move played
    if move == "A":
        move_score = 1
    elif move == "B":
        move_score = 2
    else:
        move_score = 3

    return game_score + move_score


if __name__ == "__main__":
    main()
