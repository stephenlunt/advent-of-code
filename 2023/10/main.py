# https://adventofcode.com/2023/day/10

# Very messy (especially part 2), but works - to be tidied up if I get time.


def main():
    p1()
    p2()


def parse():
    with open("./2023/10/input.txt") as f:
        return [list(row) for row in f.read().splitlines()]


def find_start(data: list[list[str]]):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "S":
                return (row, col)


def find_next(data: list[list[str]], pos: tuple[int, int], prev_dir: str):
    row, col = pos
    pipe = data[row][col]

    match pipe:
        case "|":
            if prev_dir == "S":
                return (row + 1, col), "S"
            return (row - 1, col), "N"
        case "-":
            if prev_dir == "E":
                return (row, col + 1), "E"
            return (row, col - 1), "W"
        case "L":
            if prev_dir == "S":
                return (row, col + 1), "E"
            return (row - 1, col), "N"
        case "J":
            if prev_dir == "S":
                return (row, col - 1), "W"
            return (row - 1, col), "N"
        case "7":
            if prev_dir == "E":
                return (row + 1, col), "S"
            return (row, col - 1), "W"
        case "F":
            if prev_dir == "W":
                return (row + 1, col), "S"
            return (row, col + 1), "E"
        case _:
            return (row, col), "STOP"


def p1():
    data = parse()
    start_row, start_col = find_start(data)
    pos, prev_dir = (start_row - 1, start_col), "N"  # Hard coded first move :/
    pipe_count = 0

    while prev_dir != "STOP":
        pos, prev_dir = find_next(data, pos, prev_dir)
        pipe_count += 1

    print("p1:", int(pipe_count / 2))


def p2():
    data = parse()
    start_row, start_col = find_start(data)
    pos, prev_dir = (start_row - 1, start_col), "N"
    in_loop = [pos]

    while prev_dir != "STOP":
        pos, prev_dir = find_next(data, pos, prev_dir)
        in_loop.append(pos)

    # By expanding grid to 3x scale, you can determine true inner positions through search.
    height, width = len(data), len(data[0])
    grid = []
    for _ in range(height * 3):
        grid.append(["." for _ in range(width * 3)])

    for row in range(len(data)):
        for col in range(len(data[row])):
            pipe = data[row][col]
            if (row, col) not in in_loop:
                continue

            if pipe == ".":
                continue

            if pipe == "|":
                grid[row * 3][col * 3] = "|"
                grid[row * 3 - 1][col * 3] = "|"
                grid[row * 3 + 1][col * 3] = "|"

            if pipe == "-":
                grid[row * 3][col * 3] = "-"
                grid[row * 3][col * 3 - 1] = "-"
                grid[row * 3][col * 3 + 1] = "-"

            if pipe == "L":
                grid[row * 3][col * 3] = "L"
                grid[row * 3][col * 3 + 1] = "-"
                grid[row * 3 - 1][col * 3] = "|"

            if pipe == "J":
                grid[row * 3][col * 3] = "J"
                grid[row * 3][col * 3 - 1] = "-"
                grid[row * 3 - 1][col * 3] = "|"

            if pipe == "7":
                grid[row * 3][col * 3] = "7"
                grid[row * 3][col * 3 - 1] = "-"
                grid[row * 3 + 1][col * 3] = "|"

            if pipe == "F":
                grid[row * 3][col * 3] = "F"
                grid[row * 3][col * 3 + 1] = "-"
                grid[row * 3 + 1][col * 3] = "|"

            if pipe == "S":
                grid[row * 3][col * 3] = "|"
                grid[row * 3 - 1][col * 3] = "|"
                grid[row * 3 + 1][col * 3] = "|"

    q = [(0, 0)]
    seen = set()
    while len(q) != 0:
        pos = q.pop(0)

        if pos in seen:
            continue

        add_to_q = search(grid, pos)

        for y, x in add_to_q:
            grid[y][x] = " "
            q.append((y, x))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            opts = [
                (-1, 0),
                (-2, 0),
                (0, 1),
                (0, 2),
                (1, 0),
                (2, 0),
                (0, -1),
                (0, -2),
                (-1, -1),
                (-1, 1),
                (1, 1),
                (1, -1),
                (-2, -2),
                (-2, 2),
                (2, 2),
                (2, -2),
            ]
            checks = []
            for y, x in opts:
                try:
                    if grid[i + y][j + x] != ".":
                        checks.append(False)
                    else:
                        checks.append(True)
                except IndexError:
                    pass

            if all(checks):
                grid[i][j] = "*"
                count += 1

    with open("./2023/10/visualisation.txt", "w") as f:
        for row in grid:
            for col in row:
                f.write(col)
            f.write("\n")

    print("p2:", count)


def search(grid: list[list[str]], pos: tuple[int, int]):
    row, col = pos
    opts = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    add_to_q = []

    for y, x in opts:
        if grid[row + y][col + x] == ".":
            add_to_q.append((row + y, col + x))

    return add_to_q


if __name__ == "__main__":
    main()
