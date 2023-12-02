# https://adventofcode.com/2023/day/2


def main():
    p1()
    p2()


def parse_input():
    parsed_input = {}
    with open("./2023/02/input.txt") as f:
        for line in f.read().splitlines():
            id = line.split(":")[0].split(" ")[1]
            games = line.split(": ")[1].split("; ")
            parsed_input[id] = games
    return parsed_input


def p1():
    parsed_input = parse_input()
    impossibles = set()
    red, green, blue = 12, 13, 14

    for game_id, games in parsed_input.items():
        for game in games:
            for round in [x.split(" ") for x in game.split(", ")]:
                if round[1] == "red" and int(round[0]) > red:
                    impossibles.add(game_id)
                elif round[1] == "green" and int(round[0]) > green:
                    impossibles.add(game_id)
                elif round[1] == "blue" and int(round[0]) > blue:
                    impossibles.add(game_id)

    sum = 0
    for game_id in parsed_input.keys():
        if game_id not in impossibles:
            sum += int(game_id)

    print("p1: ", sum)


def p2():
    parsed_input = parse_input()
    sum = 0

    for games in parsed_input.values():
        current_game = {"red": 0, "green": 0, "blue": 0}

        for game in games:
            for round in [x.split(" ") for x in game.split(", ")]:
                color = round[1]
                curr_val = int(round[0])
                curr_min_val = current_game[color]

                if curr_min_val == 0 or curr_min_val < curr_val:
                    current_game[color] = curr_val

        pow = 1
        for n in list(current_game.values()):
            pow *= n
        sum += pow

    print("p2: ", sum)


if __name__ == "__main__":
    main()
