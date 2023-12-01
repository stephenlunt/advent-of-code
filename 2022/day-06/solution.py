"""
https://adventofcode.com/2022/day/6
"""

def main():
    with open("./day-06/input.txt") as f:
        data = f.read()

    print(f"Problem One: {detect_distinct(data, 4)} \nProblem Two: {detect_distinct(data, 14)}")


def detect_distinct(data: str, n: int) -> int:
    for i in range(len(data)):
        # Slice the data from the current position to n.
        marker = data[i:i + n]
        
        # Converting to a set will remove duplicates, hence we can return when the set size is n.
        if len(set(marker)) == n:
            return i + n


if __name__ == "__main__":
    main()
