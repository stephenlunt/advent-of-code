# https://adventofcode.com/2023/day/11

from itertools import combinations


def main():
    p1()
    p2()


def p1():
    combis = get_combinations(1)

    sum = 0
    for pair in combis:
        sum += path(*pair)

    print("p1:", sum)


def p2():
    combis = get_combinations(1000000 - 1)

    sum = 0
    for pair in combis:
        sum += path(*pair)

    print("p2:", sum)


def parse():
    with open("./2023/11/input.txt") as f:
        return [list(row) for row in f.read().splitlines()]


def get_galaxy_locs(data: list[list[str]]):
    galaxies, y_gals, x_gals = [], set(), set()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "#":
                galaxies.append((y, x))
                y_gals.add(y)
                x_gals.add(x)

    return galaxies, y_gals, x_gals


def add_rows(
    galaxies: list[tuple[int, int]], y_gals: set[int], x_gals: set[int], n: int
):
    max_y, max_x = max(y_gals), max(x_gals)
    y_offset, x_offset = 0, 0

    for i in range(max_y):
        if not i in y_gals:
            for j in range(len(galaxies)):
                y, x = galaxies[j]
                if (y - y_offset) > i:
                    galaxies[j] = (y + n, x)
            y_offset += n

    for i in range(max_x):
        if not i in x_gals:
            for j in range(len(galaxies)):
                y, x = galaxies[j]
                if (x - x_offset) > i:
                    galaxies[j] = (y, x + n)
            x_offset += n

    return galaxies


def get_combinations(n: int):
    data = parse()
    galaxies, y_gals, x_gals = get_galaxy_locs(data)
    expanded_gals = add_rows(galaxies, y_gals, x_gals, n)
    return list(combinations(expanded_gals, 2))


def path(a, b):
    y1, x1 = a
    y2, x2 = b
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan formula


if __name__ == "__main__":
    main()
