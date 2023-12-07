# https://adventofcode.com/2023/day/7

from collections import Counter


def main():
    p1()
    p2()


def parse():
    with open("./2023/07/input.txt") as f:
        return [tuple(x.split(" ")) for x in f.read().splitlines()]


def p1():
    data, hands = parse(), {}
    for hand, bid in data:
        hands[bid] = hand_ord_arr(hand, Counter(hand), "AKQJT98765432")

    print("p1:", sort_and_sum(hands))


def p2():
    data, hands = parse(), {}
    for hand, bid in data:
        c = Counter(hand)
        if c["J"] > 0 and c["J"] < 5:
            j_count = c["J"]
            c.pop("J")
            c[max(c, key=c.get)] += j_count
        hands[bid] = hand_ord_arr(hand, c, "AKQT98765432J")

    print("p2:", sort_and_sum(hands))


def hand_ord_arr(hand: str, c: Counter, strengths: str):
    arr = []
    match sorted(c.values()):
        case [5]:
            arr.append(0)
        case [1, 4]:
            arr.append(1)
        case [2, 3]:
            arr.append(2)
        case [1, 1, 3]:
            arr.append(3)
        case [1, 2, 2]:
            arr.append(4)
        case [1, 1, 1, 2]:
            arr.append(5)
        case _:
            arr.append(6)

    return arr + [strengths.index(x) for x in hand]


def sort_and_sum(hands: dict):
    sorted_hands = sorted(hands.items(), key=lambda x: x[1], reverse=True)
    return sum([rank * int(bid[0]) for rank, bid in enumerate(sorted_hands, start=1)])


if __name__ == "__main__":
    main()
