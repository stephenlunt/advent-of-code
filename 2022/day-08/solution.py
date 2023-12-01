"""
https://adventofcode.com/2022/day/8
"""

def main():
    grid = []
    with open("./day-08/input.txt") as f:
        for row in f:
            grid.append(list(map(int, row.strip())))  # Create 2D array

    print(f"Problem 1: {p1(grid, len(grid[0]))}, Problem 2: {p2(grid, len(grid[0]))}")


def p1(grid: list[list], n: int) -> int:
    visible = (n * 4) - 4  # Initialise to outside edge

    for i in range(n):
        for j in range(n):
            if i in [0, n - 1] or j in [0, n - 1]:
                continue

            height = grid[i][j]
            row = grid[i]
            if all(x < height for x in row[:j]) or all(x < height for x in row[j + 1 :]):
                visible += 1
                continue

            col = [val[j] for val in grid]
            if all(x < height for x in col[:i]) or all(x < height for x in col[i + 1 :]):
                visible += 1

    return visible


def p2(grid: list[list], n: int) -> int:
    highest = 0

    for i in range(n):
        for j in range(n):
            if i in [0, n - 1] or j in [0, n - 1]:
                continue

            trees = 1
            height = grid[i][j]
            
            left, right = grid[i][:j], grid[i][j + 1 :]
            col = [val[j] for val in grid]
            up, down = col[:i], col[i + 1 :]

            directions = [left[::-1], right, up[::-1], down]
            for row in directions:
                trees = trees * count_trees(row, height)

            if trees > highest:
                highest = trees

    return highest


def count_trees(row: list, height: int) -> int:
    count = 1
    for val in row:
        if val >= height:
            return count
        count += 1

    return count - 1


if __name__ == "__main__":
    main()
