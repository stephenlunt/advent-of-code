"""
https://adventofcode.com/2022/day/10
"""

def main():
    with open("./day-10/input.txt") as f:
        instructions = [ i.strip() for i in f.readlines() ]
    
    x_values = [1]
    for instruction in instructions:
        if instruction == "noop":
            x_values.append(0)
        else:
            x_values.append(0)
            x_values.append(int(instruction[5:]))

    print(f"Problem One: {p1(x_values)}\n")
    print("Problem Two:")
    p2(x_values)


def p1(x_values: list) -> int:
    cycles = [20, 60, 100, 140, 180, 220]
    return sum([ sum(x_values[0:cycles[i]]) * cycles[i] for i in range(6) ])

        
def p2(x_values: list) -> None:
    screen = ["."] * 240
    new_lines = [40, 80, 120, 160, 200, 240]
    row = 0

    for i in range(len(x_values)):
        if i in new_lines:
            row += 40
        
        x = sum(x_values[0:i + 1]) + row
        sprite = [x - 1, x, x + 1]

        if i in sprite:
            screen[i] = "#"

    # Print answer
    for i in range(len(screen)):
        print(screen[i], end="")
        if (i + 1) in new_lines:
            print()


if __name__ == "__main__":
    main()
