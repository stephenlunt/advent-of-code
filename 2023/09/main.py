# https://adventofcode.com/2023/day/9


def main():
    p1()
    p2()


def parse():
    with open("./2023/09/input.txt") as f:
        rows = [line.split(" ") for line in f.read().splitlines()]
        return [list(map(lambda x: int(x), row)) for row in rows]


def p1():
    data, total = parse(), 0

    for row in data:
        accumulator = [row]
        while accumulator[-1].count(0) != len(accumulator[-1]):
            tmp = []
            for i in range(len(accumulator[-1]) - 1):
                tmp.append(accumulator[-1][i + 1] - accumulator[-1][i])
            accumulator.append(tmp)

        total += sum([row[-1] for row in accumulator])

    print("p1:", total)


def p2():
    data, total = parse(), 0

    for row in data:
        accumulator = [row]
        while accumulator[-1].count(0) != len(accumulator[-1]):
            tmp = []
            for i in range(len(accumulator[-1]) - 1):
                tmp.append(accumulator[-1][i + 1] - accumulator[-1][i])
            accumulator.append(tmp)

        accumulator = accumulator[::-1]
        prev_first_num = 0
        for i in range(len(accumulator) - 1):
            next_row_val = accumulator[i + 1][0]
            prev_first_num = next_row_val - prev_first_num

        total += prev_first_num

    print("p2:", total)


if __name__ == "__main__":
    main()
