assignments = []

def main():
    with open("./day-04/input.txt") as f:
        for row in f:
            data = row.strip().split(",")
            
            # Extract the two elves assignments as ints
            first_start, first_end = [ int(x) for x in data[0].split("-") ]
            sec_start, sec_end = [ int(x) for x in data[1].split("-") ]
            
            assignments.append([first_start, first_end, sec_start, sec_end])

    print(problem_one())
    print(problem_two())


def problem_one() -> int:
    overlaps = 0
    
    for a in assignments:
        # Check first elf overlap
        if a[0] >= a[2] and a[1] <= a[3]:
            overlaps += 1
        # Check second elf overlap
        elif a[2] >= a[0] and a[3] <= a[1]:
            overlaps += 1

    return overlaps


def problem_two() -> int:
    overlaps = 0

    for a in assignments:
        # Checks if the first elf starts within the seconds elf assignments
        if a[3] >= a[0] >= a[2]:
            overlaps += 1
        # Perform the same check for the second elf
        elif a[1] >= a[2] >= a[0]:
            overlaps += 1

    return overlaps
        

if __name__ == "__main__":
    main()
