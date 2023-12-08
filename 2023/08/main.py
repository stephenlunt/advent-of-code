# https://adventofcode.com/2023/day/8

from math import lcm


def main():
    p1()
    p2()


def parse():
    network, start_nodes = {}, []
    with open("./2023/08/input.txt") as f:
        instructions, data = tuple(f.read().split("\n\n"))
        for node in data.split("\n"):
            key = node.split(" = ")[0]
            left, right = tuple(
                node.split(" = ")[1].removeprefix("(").removesuffix(")").split(", ")
            )
            network[key] = {"L": left, "R": right}

            if key[-1] == "A":
                start_nodes.append(key)
    return list(instructions), network, start_nodes


def p1():
    instructions, network, _ = parse()

    count = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        options = network[current_node]
        current_instruction = instructions.pop(0)
        instructions.append(current_instruction)
        current_node = options[current_instruction]
        count += 1

    print("p1:", count)


def p2():
    instructions, network, start_nodes = parse()
    multiples = []

    for node in start_nodes:
        count = 0
        current_node = node
        tmp_instructions = instructions.copy()
        while True:
            options = network[current_node]
            current_instruction = tmp_instructions.pop(0)
            tmp_instructions.append(current_instruction)
            current_node = options[current_instruction]
            count += 1

            if current_node[-1] == "Z":
                multiples.append(count)
                break

    print("p2:", lcm(*multiples))


if __name__ == "__main__":
    main()
