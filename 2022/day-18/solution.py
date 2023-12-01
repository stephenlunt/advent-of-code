"""
https://adventofcode.com/2022/day/18
"""

cubes, faces = [], []

def main():
    global cubes

    data = open("./day-18/input.txt").read().splitlines()
    for cube in data:
        x, y, z = list(map(int, cube.split(",")))
        cubes.append((x, y, z))

    total_surface = p1()
    print(f"Problem One: {total_surface}")

    outside_surface = total_surface - p2(25)
    print(f"Problem Two: {outside_surface}")


def p1() -> int:
    global cubes, faces
    
    points = [
        [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)],
        [(0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)],
        [(0, 0, 0), (0, 0, 1), (1, 0, 1), (1, 0, 0)],
        [(0, 1, 0), (0, 1, 1), (1, 1, 1), (1, 1, 0)],
        [(0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 0)],
        [(1, 0, 0), (1, 0, 1), (1, 1, 1), (1, 1, 0)]
    ]
    
    for cube in cubes:
        for p in points:
            append_face(cube, p)

    total_surfaces = 0
    for face in faces:
        if faces.count(face) == 1: total_surfaces += 1
    
    return total_surfaces


def append_face(cube: list, points: list[tuple]) -> None:
    global faces

    x, y, z = cube
    face = []
    [face.append((x + px, y + py, z + pz)) for px, py, pz in points]
    faces.append(face)


def p2(MATRIX_SIZE: int) -> int:
    matrix = []
    grid = [["."] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]

    for i in range(MATRIX_SIZE):
        # Build grid layer by layer
        for c in cubes:
            if c[2] == i:
                grid[c[0]][c[1]] = "#"
        
        for y in range(MATRIX_SIZE):
            inside = False
            for x in range(MATRIX_SIZE - 1):
                if grid[y][x] == "#" and grid[y][x + 1] == "." and grid[y][x:].count("#") > 1:
                    inside = True
                elif inside is True and grid[y][x] == "#":
                    inside = False
                elif inside is True and grid[y][x] != "#":
                    grid[y][x] = "o" # Set blocks encapsulated inside the cube to "o" for air
                
        matrix.append(grid)
        grid = [["."] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]


    N, face_count = 0, 0
    points = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    
    # TODO: Improve efficiency of filling air gaps at edges without iterating over data.
    while N < 5:
        for z, layer in enumerate(matrix):
            for y in range(MATRIX_SIZE):
                for x in range(MATRIX_SIZE):
                    if layer[y][x] == "o":
                        for px, py, pz in points:
                            if matrix[z + pz][y + py][x + px] == ".":
                                layer[y][x] = "."

                    if N == 4 and layer[y][x] == "o":
                        for px, py, pz in points:
                            if matrix[z + pz][y + py][x + px] == "#":
                                face_count += 1
        N += 1

    return face_count


if __name__ == "__main__":
    main()
