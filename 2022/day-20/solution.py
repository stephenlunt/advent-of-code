"""
https://adventofcode.com/2022/day/20
"""

def main():
    seq = []
    with open("./day-20/input.txt") as f:
        for row in f:
            item = (int(row.strip()), False)
            seq.append(item)

    print(p1(seq))


def p1(seq: list) -> int:
    i, n = 0, len(seq)
    
    while True:
        if i == n:
            break

        val, seen = seq[i]

        if not seen:
            if val == 0:
                seq[i] = (0, True)
                i0 = i

            else:
                new_index = i + val
                if new_index == 0:
                    new_index -= 1
                elif new_index > n:
                    new_index -= n
                
                seq.pop(i)
                seq.insert(new_index, (val, True))
            i = 0
        else:
            i += 1

    n1000 = seq[(1000 - i0) % n][0]
    n2000 = seq[(2000 - i0) % n][0]
    n3000 = seq[(3000 - i0) % n][0]

    return n1000 + n2000 + n3000




if __name__ == "__main__":
    main()
