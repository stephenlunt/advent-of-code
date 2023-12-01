# https://adventofcode.com/2023/day/1


def main():
    p1()
    p2()


def p1():
    sum = 0

    with open("./2023/01/input.txt") as f:
        for line in f.read().splitlines():
            num = ""

            for ch in line:
                if ch.isdigit():
                    num += ch
                    break

            for ch in line[::-1]:
                if ch.isdigit():
                    num += ch
                    break

            sum += int(num)

    print("p1: ", sum)


def p2():
    sum = 0

    with open("./2023/01/input.txt") as f:
        for line in f.read().splitlines():
            num = ""
            num += check_values(line, False)
            num += check_values(line[::-1], True)
            sum += int(num)

    print("p2: ", sum)


def check_values(arr: list[str], backwards: bool) -> str:
    nums_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    num, seen = "", ""

    for ch in arr:
        if ch.isdigit():
            num += ch
            return num

        seen += ch
        for k, v in nums_map.items():
            if not backwards:
                if k in seen:
                    num += v
                    return num
            else:
                if k in seen[::-1]:
                    num += v
                    return num


if __name__ == "__main__":
    main()
