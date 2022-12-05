"""
https://adventofcode.com/2022/day/5
"""

storage = {}
moves = []

def main():
    # Read in both the existing crate layout and moves
    read_existing_storage()
    read_moves()

    problem = input("Which problems (1/2): ")

    if problem == "1":
        # Execute moves and print ans to problem one
        exec_moves()
        print(problem_one())
    elif problem == "2":
        # Execute moves and print ans to problem two
        exec_moves_with_cratemover9001()
        print(problem_two())



def read_existing_storage():
    crates = []

    with open("./day-05/input.txt") as f:
        for line in f:
            # Get the line break
            if line == "\n":
                break

            line = list(line)
            row = []
            index = 0
            for _ in range(9):
                crate = "".join(line[index:index+4])
                row.append(crate.strip())
                index += 4
            
            crates.append(row)

        for num in crates[-1]:
            storage[num] = []
        crates.pop(-1)

        for i in range(len(crates) + 1):
            col = i + 1
            for j in range(8):
                if crates[j][i] == "":
                    continue
                else:
                    c = crates[j][i].replace("[", "").replace("]", "")
                    storage[str(col)].append(c)


def read_moves():
    with open("./day-05/input.txt") as f:
        for line in f:
            if line.startswith("[") or line.startswith(" ") or line == "\n":
                continue

            line = line.strip().split(" ")
            line.remove("move")
            line.remove("from")
            line.remove("to")
            moves.append(line)


def exec_moves():
    for move in moves:
        n = int(move[0])
        old_col = move[1]
        new_col = move[2]

        for _ in range(n):
            # 0 index will always be the crate on top
            crate_to_move = storage[old_col][0]
            storage[old_col].pop(0)
            storage[new_col].insert(0, crate_to_move)


def problem_one():
    ans = ""
    for key in storage.keys():
        ans = ans + storage[key][0]
    return ans


def exec_moves_with_cratemover9001():
    for move in moves:
        n = int(move[0])
        old_col = move[1]
        new_col = move[2]

        stack = []
        for _ in range(n):
            crate_to_move = storage[old_col][0]
            storage[old_col].pop(0)
            stack.append(crate_to_move)

        for i in range(n):
            crate_to_place = stack[n - 1 - i]
            storage[new_col].insert(0, crate_to_place)


def problem_two():
    ans = ""
    for key in storage.keys():
        ans = ans + storage[key][0]
    return ans


if __name__ == "__main__":
    main()
