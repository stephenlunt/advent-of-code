"""
https://adventofcode.com/2022/day/13
"""

def main():
    print(f"Sum of indices: {p1()}")
    print(f"Decoder key: {p2()}")


def p1() -> int:
    packets = [x.split("\n") for x in open("./day-13/input.txt").read().split("\n\n")]
    sum = 0

    for index, (p1, p2) in enumerate(packets, start=1):
        left, right = eval(p1), eval(p2)
        cmp_value = cmp(left, right) # Recursive function to unpack lists and get values
        if cmp_value < 0:
            sum += index
    
    return sum


def p2() -> int:
    packets = [x for x in open("./day-13/input.txt").read().splitlines()]
    index2, index6 = 0, 0
    
    for p in packets:
        if p == "":
            continue
        
        pkt = eval(p)
        # For each packet, if it's comparison value is less than the divider packet, up the indices by 1
        if cmp(pkt, [[2]]) < 0:
            index2 += 1
        if cmp(pkt, [[6]]) < 0:
            index6 += 1

    return (index2 + 1) * (index6 + 2) # Add 1 & 2 to account for starting positions


def cmp(left, right) -> int:
    # Compare lists
    if type(left) is list and type(right) is list:
        # Unpack values
        for lv, rv in list(zip(left, right)):
            return_val = cmp(lv, rv)
            if return_val:
                return return_val
        
        return len(left) - len(right)
    
    # Compare ints
    if type(left) is int and type(right) is int:
        return left - right

    # Convert int types to list
    if type(left) is list:
        return cmp(left, [right])
    elif type(right) is list:
        return cmp([left], right)


if __name__ == "__main__":
    main()
