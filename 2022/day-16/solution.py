"""
https://adventofcode.com/2022/day/16
"""

from collections import deque

valves = {}
vectors = {}


def main():
    parse()
    print(valves)
    print(vectors)
    p1()


def parse():
    global valves, vectors, start_value

    lines = open("./day-16/input.txt").read().splitlines()
    for line in lines:
        name = line[6:8]
        rate = int(line[line.index("=") + 1 : line.index(";")])
        valves[name] = rate

        line = line[line.index(";") :]
        i, to = 0, []
        while i < len(line):
            if line[i].isupper():
                to.append(f"{line[i]}{line[i + 1]}")
                i += 2
            else:
                i += 1

        vectors[name] = to


# BFS
def p1():
    queue = ["AA"]
    visited = ["AA"]
    reward = 0

    while queue:
        valve = queue.pop(0)

        for node in vectors[valve]:
            if node not in visited:
                print(node)
                reward += valves[node]
                visited.append(node)
                [queue.append(n) for n in vectors[node] if n not in visited]

    print(reward)


if __name__ == "__main__":
    main()
