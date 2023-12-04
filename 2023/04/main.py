# https://adventofcode.com/2023/day/4


def main():
    p1()
    p2()


def p1():
    sum = 0

    with open("./2023/04/input.txt") as f:
        for line in f.read().splitlines():
            nums = line.split(": ")[1].split(" | ")
            winning_nums = [x for x in nums[0].split(" ") if x != ""]
            matching_nums = [x for x in nums[1].split(" ") if x in winning_nums]

            if matching_nums:
                sum += 1 * 2 ** (len(matching_nums) - 1)

    print("p1:", sum)


def p2():
    cards_list = []

    with open("./2023/04/input.txt") as f:
        for line in f.read().splitlines():
            nums = line.split(": ")[1].split(" | ")
            winning_nums = [x for x in nums[0].split(" ") if x != ""]
            wins_per_card = len([x for x in nums[1].split(" ") if x in winning_nums])
            cards_list.append(wins_per_card)

    counts = {}

    for card_no, n_wins in enumerate(cards_list):
        if card_no not in counts:
            counts[card_no] = 1

        for i in range(card_no + 1, card_no + 1 + n_wins):
            if i not in counts:
                counts[i] = 1 + counts[card_no]
            else:
                counts[i] += counts[card_no]

    print("p2:", sum(counts.values()))


if __name__ == "__main__":
    main()
