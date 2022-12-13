def main():
    # Initialise a list to store each elfs total cals.
    totals = list()

    # Read the input file
    with open("./day-01/input.txt") as f:
        total = 0
        for row in f:
            # New line indiciators a new elf to total.
            if row == "\n":
                totals.append(total)
                total = 0
            else:
                # Increment total.
                total += int(row.rstrip("\n"))
        

    # Print the elf with the most cals.
    print(f"Max cals: {max(totals)}")

    # Get the sum of the top three elves cals
    print(f"Top 3 elves cals: {top_three_elfs(totals)}")


def top_three_elfs(totals: list) -> int:
    totals.sort(reverse = True)
    
    top3 = 0
    for i in range(3):
        top3 += totals[i]
    
    return top3


if __name__ == "__main__":
    main()
