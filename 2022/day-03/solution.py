rucksacks = []

def main():
    read_file()
    print(problem_one())
    print(problem_two())


def read_file():
    with open("./day-03/input.txt") as f:
        for row in f:
            rucksacks.append(row)


def problem_one() -> int:
    sum = 0

    for rucksack in rucksacks:
        # Split each rucksack into two equal compartments
        n = int(len(rucksack) / 2)
        first_compartment = rucksack[0:n]
        second_compartment = rucksack[n:-1]

        for letter in first_compartment:
            if letter in second_compartment:
                # Do a bit of maths with the ascii values to get the priority
                if letter.islower():
                    sum += ord(letter) - 96
                    break
                else:
                    sum += ord(letter) - 38
                    break

    return sum


def problem_two() -> int:
    # Divide the rucksacks into three groups
    n = int(len(rucksacks) / 3)
    sum = 0
    index = 0

    for _ in range(n):
        for letter in rucksacks[index]:
            if letter in rucksacks[index + 1] and letter in rucksacks[index + 2]:
                if letter.islower():
                    sum += ord(letter) - 96
                    break
                else:
                    sum += ord(letter) - 38
                    break
        
        index += 3

    return sum
        

if __name__ == "__main__":
    main()
