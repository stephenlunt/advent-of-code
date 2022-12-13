"""
https://adventofcode.com/2022/day/12
"""

def main():
    with open("./day-12/input.txt") as f:
        grid = [ list(row) for row in f.read().split("\n") ]

    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item == "S": 
                start = [0, i, j]
                grid[i][j] = "a"
            elif item == "E": 
                grid[i][j] = "z"
            
            row[j] = ord(grid[i][j]) - 97
    
    print(f"Problem One: {p1(grid, start)}")
    print(f"Problem Two: {p2(grid)}")


# Breadth-first search
def p1(grid: list[list], start: list) -> int:
    queue = [start]
    explored = set((start[1], start[2]))
    rows, cols = len(grid), len(grid[0])

    while queue:
        distance, i, j = queue[0]
        queue.pop(0)

        for n in [-1, 1]:
            # Y axis neighbours
            if (i + n) < 0 or (i + n) >= rows or (i + n, j) in explored:
                pass
            elif grid[i + n][j] - grid[i][j] > 1:
                pass
            elif grid[i + n][j] == 25:
                return distance + 1
            else:
                explored.add((i + n, j))
                queue.append([distance + 1, i + n, j])

            # X axis neighbours
            if (j + n) < 0 or (j + n) >= cols or (i, j + n) in explored:
                pass
            elif grid[i][j + n] - grid[i][j] > 1:
                pass
            elif grid[i][j + n] == 25:
                return distance + 1
            else:
                explored.add((i, j + n))
                queue.append([distance + 1, i, j + n])


def p2(grid: list[list]) -> int:
    starting_points = []
    distances = set()

    for i, row in enumerate(grid):
        for j in range(len(row)):
            if grid[i][j] == 0:
                starting_points.append([0, i, j])

    for point in starting_points:
        d = p1(grid, point)
        if d is not None:
            distances.add(d)

    return min(distances)


if __name__ == "__main__":
    main()
