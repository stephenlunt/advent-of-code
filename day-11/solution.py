"""
https://adventofcode.com/2022/day/11
"""

from math import prod

monkeys = []

def main():
    parse()

    # Today I learnt a valuable lession that running two cases back to back will not
    # produce the right answer when you modify the data without re-parsing the input :\
    # Many hours I shall not get back :)
    match input("Which problem: "):
        case "1": print("Problem 1:", run(20, 3))
        case "2": print("Problem 2:", run(10_000, 0))


def parse():
    with open("./day-11/input.txt") as f:
        lines = f.read().split("\n\n")
    
    for i, line in enumerate(lines):
        line = line.split("\n")
        m = {"id": i}
        m["items"] = [int(x) for x in line[1].strip().removeprefix("Starting items:").split(", ")]
        m["operation"] = eval(f"lambda old: {line[2].strip().removeprefix('Operation: new = ')}")
        m["test"] = int(line[3][-2:])
        m["true"] = int(line[4][-1])
        m["false"] = int(line[5][-1])
        monkeys.append(m)


def run(rounds: int, lvl: int):
    inspected = [0] * len(monkeys)

    modulo = prod([m["test"] for m in monkeys])

    for _ in range(rounds):
        for i, m in enumerate(monkeys):
            for item in m["items"]:
                wl = m["operation"](item)
                wl %= modulo

                if lvl != 0:
                    wl //= lvl
                
                if wl % m["test"] == 0:
                    monkeys[m["true"]]["items"].append(wl)
                else:
                    monkeys[m["false"]]["items"].append(wl)
                
            inspected[i] += len(m["items"])
            m["items"] = []

    return sorted(inspected)[-1] * sorted(inspected)[-2]


if __name__ == "__main__":
    main()
