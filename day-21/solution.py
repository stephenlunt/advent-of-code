"""
https://adventofcode.com/2022/day/21
"""

from math import pow

nums, ops = dict(), dict()

def main():
    parse()
    print(f"Problem One: {p1()}")
    print(f"Problem Two: {p2()}")


def parse() -> None:
    global nums, ops

    with open("./day-21/input.txt") as f:
        for row in f:
            if row[6].isdigit():
                nums[row[0:4]] = int(row[6:].strip())
            else:
                ops[row[0:4]] = row.strip().split(": ")[1]


def p1() -> int:
    global nums

    while nums.get("root") is None:
        for key, val in ops.items():
            m1, op, m2 = val.split(" ")
            
            if nums.get(m1) and nums.get(m2):
                nums[key] = eval(f"{nums[m1]} {op} {nums[m2]}")

    return nums["root"]


def p2() -> int:
    lower, upper = 0, pow(10, 16)

    while True:
        mid = (upper + lower) // 2

        ops.clear()
        nums.clear()
        parse()
        nums["humn"] = mid
        p1()

        r1, tmp, r2 = ops["root"].split(" ")
        n1, n2 = nums[r1], nums[r2]

        if n1 == n2:
            return mid
        elif n1 < n2:
            upper = mid
        else:
            lower = mid


if __name__ == "__main__":
    main()
