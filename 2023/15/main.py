# https://adventofcode.com/2023/day/15


def main():
    p1()
    p2()


def parse():
    with open("./2023/15/input.txt") as f:
        return f.read().split(",")


def p1():
    data = parse()
    current_vals = []

    for string in data:
        current_vals.append(calc_hash(string))

    print("p1:", sum(current_vals))


def p2():
    data = parse()
    hashmap: dict[list[str]] = {}

    for string in data:
        hash_val = (
            calc_hash(string[:-1])
            if string.find("-") != -1
            else calc_hash(string.split("=")[0])
        )

        if string.find("-") != -1:
            box = hashmap.get(hash_val, [])
            for i, item in enumerate(box):
                if item.startswith(string[:-1]):
                    box.pop(i)
                    break
            hashmap[hash_val] = box
        else:
            box = hashmap.get(hash_val, [])
            hash, focal_len = string.split("=")[0], string[-1]
            found = False
            for i, item in enumerate(box):
                if item.startswith(hash):
                    box.pop(i)
                    box.insert(i, f"{hash}:{focal_len}")
                    found = True
                    break
            if not found:
                box.append(f"{hash}:{focal_len}")

            hashmap[hash_val] = box

    totals = []
    for box_no, lenses in hashmap.items():
        for slot_no, lens in enumerate(lenses):
            focal_len = int(lens[-1])
            totals.append((box_no + 1) * (slot_no + 1) * focal_len)

    print("p2:", sum(totals))


def calc_hash(chars: str) -> int:
    current_val = 0
    for ch in chars:
        current_val += ord(ch)
        current_val *= 17
        current_val = current_val % 256

    return current_val


if __name__ == "__main__":
    main()
