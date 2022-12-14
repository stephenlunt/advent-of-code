"""
https://adventofcode.com/2022/day/14
"""

grid = []
mx, my = 0, 0

def its_raining_sand():
    parse()
    match input("Problemo 1 or problem 2? "):
        case "1": print(f"Units of sand: {p1()}")
        case "2": print(f"That's alot of sand... {p2()}")


def parse():
    global grid, mx, my

    # Parse paths
    paths = [x.split(" -> ") for x in open("./day-14/input.txt").read().splitlines()]
    for p in paths:
        for i in range(len(p)):
            p[i] = [int(x) for x in p[i].split(",")]
            if p[i][0] > mx: mx = p[i][0]
            if p[i][1] > my: my = p[i][1]

    # Initialise the grid
    grid = [["."] * (mx + my) for _ in range(my + 3)]

    # Fill grid with initial paths
    for p in paths:
        for i in range(len(p) - 1):
            x1, x2 = p[i][0], p[i + 1][0]
            y1, y2 = p[i][1], p[i + 1][1]
            
            if y1 - y2 < 0: # Draw down
                for i in range(y2 - y1 + 1):
                    grid[y1 + i][x1] = "#"
            elif y1 - y2 > 0: # Draw up
                for i in range(y1 - y2 + 1):
                    grid[y1 - i][x1] = "#"
            elif x1 - x2 < 0: # Draw right
                for i in range(x2 - x1 + 1):
                    grid[y1][x1 + i] = "#"
            elif x1 - x2 > 0: # Draw left
                for i in range(x1 - x2 + 1):
                    grid[y1][x1 - i] = "#"

    
def p1() -> int:
    start, i = [500, 0], 0
    
    while True:
        try:
            check(start)
            i += 1
        # The index out of bounds exception is used to tell if the sand left the grid into the void, hence we return.
        except IndexError:
            return i


def p2() -> int:
    global mx, my
    for i in range(mx + my):
        grid[-1][i] = "#" # Grid floor added

    start, i = [500, 0], 0

    while True:
        check(start)
        i += 1

        if grid[0][500] == "o":
            return i


# Recursive sand direction checking function
def check(start):
    global grid
    x, y = start
    
    if grid[y + 1][x] == ".":
        check([x, y + 1])  # Sand falls
    
    elif grid[y + 1][x] == "o" or grid[y + 1][x]:
        if grid[y + 1][x - 1] == ".": 
            check([x - 1, y + 1]) # Diagonal left
        elif grid[y + 1][x + 1] == ".": 
            check([x + 1, y + 1]) # Diagonal right
        elif grid[y][x - 1] in ["#", "o"] and grid[y][x + 1] in ["#", "o"]:
            grid[y][x] = "o"  # Comes to rest & break out recursion
            return
        else:
            grid[y][x] = "o" # Comes to rest & break recursion
            return  


if __name__ == "__main__":
    its_raining_sand()
