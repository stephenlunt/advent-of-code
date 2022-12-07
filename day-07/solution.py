"""
https://adventofcode.com/2022/day/7
"""

# Dict to store file paths and relative sizes
sizes = {}


def main():
    commands = parse()
    print(f"Problem 1: {p1(commands)}")
    print(f"Problem 2: {p2()}")


def parse() -> list:
    with open("./day-07/input.txt") as f:
        return f.readlines()


def p1(commands: list) -> int:
    full_path = "."

    for command in commands:
        c = command.strip().split(" ")

        if c[0] == "dir" or c[1] == "ls":
            continue

        # On dir change, update the full path
        elif c[0] == "$":
            if c[2] == "..":
                x = full_path.rfind("/")
                full_path = full_path[0:x]
            elif c[2] == "/":
                full_path = "."
            else:
                full_path = full_path + "/" + c[2]

        else:
            directory = full_path

            # For each file in the full path, increment by the file size found
            for _ in range(directory.count("/") + 1):
                try:
                    tmp = sizes[directory]
                except KeyError:
                    sizes[directory] = 0
                finally:
                    sizes[directory] += int(c[0])
                    x = directory.rfind("/")
                    directory = directory[0:x]

    return sum(x for x in sizes.values() if x <= 100000)


def p2() -> int:
    total_used = sizes["."]
    min_required = 30_000_000 - (70_000_000 - total_used)

    # Find the smallest positive difference in file sizes to delete
    closest = 70_000_000
    for value in sizes.values():
        diff = value - min_required
        if diff > 1 and diff < closest:
            closest = value

    return closest


if __name__ == "__main__":
    main()
