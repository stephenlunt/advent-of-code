# https://adventofcode.com/2023/day/6


def main():
    p1()
    p2()


def parse():
    with open("./2023/06/input.txt") as f:
        rows = tuple(
            list(filter(lambda x: x.isdigit(), a.split(" ")))
            for a in f.read().split("\n")
        )
        return rows


def p1():
    times, distances = parse()

    sum = 1
    for i, time in enumerate(times):
        outcomes = []
        for speed in range(int(time) + 1):
            outcomes.append((int(time) - speed) * speed)
        sum *= len([x for x in outcomes if x > int(distances[i])])

    print("p1:", sum)


def p2():
    times, distances = parse()
    time = int("".join(times))
    distance = int("".join(distances))

    count = 0
    for speed in range(time + 1):
        if ((time - speed) * speed) > distance:
            count += 1

    print("p2:", count)


if __name__ == "__main__":
    main()
