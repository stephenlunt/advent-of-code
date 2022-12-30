"""
https://adventofcode.com/2022/day/23
"""

from collections import Counter

elves = {}

def main():
    parse()
    run()


def parse():
    global elves

    for y, row in enumerate(open("./day-23/input.txt").read().splitlines()):
        for x, item in enumerate(row):
            if item == "#":
                elves[f"{x},{y}"] = (x, y)


def run():
    directions = ["N", "S", "W", "E"]
    rnd = 0

    while True:
        rnd += 1
        moves = {}

        for x, y in elves.values():
            moves[f"{x},{y}"] = propose_move(x, y, directions)

        if list(moves.values()).count("X") == len(elves):
            break
        execute_move(moves)

        # Shift directions
        directions.append(directions[0])
        directions.pop(0)

        if rnd == 10:
            print(f"Empty tiles after 10 rounds={calc_empty_tiles()}")

    print(f"Total rounds={rnd}")


def propose_move(x: int, y: int, directions: list[str]):
    N = [(x-1, y-1), (x, y-1), (x+1, y-1)]
    S = [(x-1, y+1), (x, y+1), (x+1, y+1)]
    W = [(x-1, y-1), (x-1, y), (x-1, y+1)]
    E = [(x+1, y-1), (x+1, y), (x+1, y+1)]
    P = N + S + W + E

    stay = True
    for px, py in P:
        if elves.get(f"{px},{py}") is not None:
            stay = False
            break
    if stay: return "X"

    for d in directions:
        if d == "N" and check_direction(N):
            return (x, y-1)
        elif d == "S" and check_direction(S):
            return (x, y+1)
        elif d == "W" and check_direction(W):
            return (x-1, y)
        elif d == "E" and check_direction(E):
            return (x+1, y)

    return "X"


def check_direction(points: list) -> bool:
    for x, y in points:
        if f"{x},{y}" in elves:
            return False
    return True


def execute_move(moves: dict):
    for key, value in moves.items():
        if value == "X":
            continue
        if Counter(moves.values())[value] > 1:
            continue
        else:
            # Remove old elf position and append new
            elves.pop(key)
            elves[f"{value[0]},{value[1]}"] = value


def calc_empty_tiles() -> int:
    X, Y = set(), set()

    for x, y in elves.values():
        X.add(x)
        Y.add(y)

    h = max(Y) - min(Y) + 1
    w = max(X) - min(X) + 1
    return (h * w) - len(elves)


if __name__ == "__main__":
    main()
