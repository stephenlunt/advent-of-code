strategy = []

def main():
    read_file()

    total_score = 0
    for game in strategy:
        round_score = calculate_game(game)
        total_score += round_score

    print(f"The total score was: {total_score}")


def read_file():
    with open("./day-02/input.txt") as f:
        for row in f:
            game = row.rstrip("\n").split(" ")
            strategy.append(game)


def calculate_game(game: list) -> int:
    shape_score = calculate_shape_score(game[1])

    game_outcome = did_we_win(game)
    if game_outcome == 1:
        game_score = 6
    elif game_outcome == 0:
        game_score = 3
    else:
        game_score = 0

    return shape_score + game_score


def calculate_shape_score(shape: str) -> int:
    match shape:
        case "X":  # Rock
            return 1
        case "Y":  # Paper
            return 2
        case "Z":  # Scissors
            return 3
            

def did_we_win(game: list) -> int:
    """
    Returns -1 on loss, 0 on draw and +1 on win.
    """
    # Check for winning scenerios
    if game[0] == "A" and game[1] == "Y":
        return 1  # Paper beats rock
    elif game[0] == "B" and game[1] == "Z":
        return 1  # Scissors beat paper
    elif game[0] == "C" and game[1] == "X":
        return 1  # Rock beats scissors

    # Check for draws (by checking the difference in ascii values)
    if ord(game[1]) - ord(game[0]) == 23:
        return 0

    return -1


if __name__ == "__main__":
    main()
