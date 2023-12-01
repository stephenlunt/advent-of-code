"""
https://adventofcode.com/2022/day/25
"""

def main():
    seq = [x for x in open("./day-25/input.txt").read().split("\n")]
    print(f"Problem One: {p1(seq)}")


def p1(seq: list[str]) -> str:
    total = 0

    for num in seq:
        n = len(num)

        for i, x in enumerate(num):
            match x:
                case "-":
                    x = -1
                case "=":
                    x = -2
                case _:
                    x = int(x)

            p = n - 1 - i
            total += x * (5**p)

    return dec_to_snafu(total)


def dec_to_snafu(num: int) -> str:
    snafu = ""
    ops = ["-", "="]

    while num != 0:
        r = num % 5
        num = num // 5

        if r <= 2:
            snafu = str(r) + snafu
        else:
            snafu = ops[r - 4] + snafu
            num += 1

    return snafu


if __name__ == "__main__":
    main()
