# https://adventofcode.com/2023/day/16


def main():
    p1()
    p2()


def parse():
    grid = {}
    with open("./2023/16/input.txt") as f:
        data = f.read().splitlines()

        for y, row in enumerate(data):
            for x, val in enumerate(row):
                grid[f"{y},{x}"] = val

    return grid, data


def p1():
    grid, _ = parse()
    seen = set()
    queue = [(0, 0, 0, 1)]

    while queue:
        state = queue.pop(0)
        y, x, *_ = state

        if state in seen:
            continue

        next_moves = get_next_moves(grid, state)
        for move in next_moves:
            if move is not []:
                queue.append(move)

        seen.add(state)

    energised = set()
    for y, x, *_ in seen:
        if f"{y},{x}" in grid:
            energised.add(f"{y},{x}")

    print("p1:", len(energised))


def p2():
    grid, data = parse()
    starting_points = []

    for i in range(len(data)):
        starting_points.append((i, 0, 0, 1))
        starting_points.append((i, len(data[0]) - 1, 0, -1))

    for i in range(len(data[0])):
        starting_points.append((0, i, 1, 0))
        starting_points.append((len(data) - 1, i, -1, 0))

    highest_config = 0

    for point in starting_points:
        seen = set()
        queue = [point]

        while queue:
            state = queue.pop(0)
            y, x, *_ = state

            if state in seen:
                continue

            next_moves = get_next_moves(grid, state)
            for move in next_moves:
                if move is not []:
                    queue.append(move)

            seen.add(state)

        energised = set()
        for y, x, *_ in seen:
            if f"{y},{x}" in grid:
                energised.add(f"{y},{x}")

        if len(energised) > highest_config:
            highest_config = len(energised)

    print("p2:", highest_config)


def get_next_moves(grid: dict, state: tuple[int]) -> list[tuple[int]]:
    y, x, dy, dx = state

    try:
        val = grid[f"{y},{x}"]
    except KeyError:
        return []

    if val == ".":
        return [(y + dy, x + dx, dy, dx)]

    # UP
    if dy == -1:
        if val == "|":
            return [(y - 1, x, -1, 0)]
        if val == "-":
            return [(y, x - 1, 0, -1), (y, x + 1, 0, 1)]
        if val == "/":
            return [(y, x + 1, 0, 1)]
        if val == "\\":
            return [(y, x - 1, 0, -1)]

    # DOWN
    if dy == 1:
        if val == "|":
            return [(y + 1, x, 1, 0)]
        if val == "-":
            return [(y, x - 1, 0, -1), (y, x + 1, 0, 1)]
        if val == "/":
            return [(y, x - 1, 0, -1)]
        if val == "\\":
            return [(y, x + 1, 0, 1)]

    # RIGHT
    if dx == 1:
        if val == "-":
            return [(y, x + 1, 0, 1)]
        if val == "|":
            return [(y - 1, x, -1, 0), (y + 1, x, 1, 0)]
        if val == "/":
            return [(y - 1, x, -1, 0)]
        if val == "\\":
            return [(y + 1, x, 1, 0)]

    # LEFT
    if dx == -1:
        if val == "-":
            return [(y, x - 1, 0, -1)]
        if val == "|":
            return [(y - 1, x, -1, 0), (y + 1, x, 1, 0)]
        if val == "/":
            return [(y + 1, x, 1, 0)]
        if val == "\\":
            return [(y - 1, x, -1, 0)]


if __name__ == "__main__":
    main()
