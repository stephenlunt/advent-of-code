# https://adventofcode.com/2023/day/3


def main():
    with open("./2023/03/input.txt") as f:
        data = f.read().split("\n")

    p1(data)
    p2(data)


def p1(data: list[str]):
    nums = enumerate_arr(data, True)
    print("p1:", sum(nums))


def p2(data: list[str]):
    gears = enumerate_arr(data, False)

    sum = 0
    for parts in gears.values():
        if len(parts) == 2:
            sum += int(parts[0]) * int(parts[1])

    print("p2:", sum)


def enumerate_arr(data: list[str], p1: bool):
    nums, gears = [], {}
    for i, row in enumerate(data):
        num = ""
        start, end = None, None
        for j, ch in enumerate(row):
            if not ch.isdigit() and num == "":
                continue
            elif num == "":
                num += ch
                start = (i, j)
            else:
                if ch != ".":
                    num += ch

                if j + 1 == len(data[i]) or not data[i][j + 1].isdigit() or ch == ".":
                    end = (i, j) if ch != "." else (i, j - 1)

                    if p1:
                        valid = check_neighbours(data, start, end, False)
                        if valid is not None:
                            nums.append(int(num))
                    else:
                        gear = check_neighbours(data, start, end, True)
                        if gear is not None:
                            if gear in gears:
                                val = gears[gear]
                                val.append(num)
                                gears[gear] = val
                            else:
                                gears[gear] = [num]

                    num = ""

    return nums if p1 else gears


def check_neighbours(
    data: list[str], start: tuple[int, int], end: tuple[int, int], p2: bool
) -> bool:
    spec_chars = {"*"} if p2 else {"*", "%", "$", "=", "#", "&", "/", "@", "+", "-"}
    opts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for sy, sx in [start, end]:
        for y, x in opts:
            i = sy + y
            j = sx + x

            if i < 0 or j < 0:
                continue
            try:
                if data[i][j] in spec_chars:
                    return f"{i},{j}"
            except IndexError:
                continue

    return None


if __name__ == "__main__":
    main()
