"""
https://adventofcode.com/2022/day/17
"""

jet_movements = []
shapes = [1, 2, 3, 4, 5]
fallen_rocks = set()


def main():
    parse()
    p1()


def parse():
    global jet_movements
    jet_movements = list(open("./day-17/input.txt").read())


def p1():
    global fallen_rocks
    base = 0

    for i in range(2022):
        shape_number = shapes.pop(0)
        shapes.append(shape_number)
        shape_points = get_shape(shape_number, base)

        while True:
            jet_direction = jet_movements.pop(0)
            jet_movements.append(jet_direction)

            shape_points = jet_push(jet_direction, shape_points)
            if fall(shape_points) == False:
                max_y = shape_points[0][1]
                for p in shape_points:
                    fallen_rocks.add(p)
                    if p[1] > max_y:
                        base = p[1]
                break
            else:
                shape_points = fall(shape_points)

    print(i, base)


def get_shape(num: int, base: int):
    match num:
        case 1:
            return [(3, base + 4), (4, base + 4), (5, base + 4), (6, base + 4)]
        case 2:
            return [
                (3, base + 5),
                (4, base + 5),
                (5, base + 5),
                (4, base + 4),
                (4, base + 6),
            ]
        case 3:
            return [
                (3, base + 4),
                (4, base + 4),
                (5, base + 4),
                (5, base + 5),
                (5, base + 6),
            ]
        case 4:
            return [(3, base + 4), (3, base + 5), (3, base + 6), (3, base + 7)]
        case 5:
            return [(3, base + 4), (4, base + 4), (3, base + 5), (3, base + 5)]


def jet_push(jet_direction, shape_points):
    global fallen_rocks

    mutated_points = mutate_points(jet_direction, shape_points)

    for p in mutated_points:
        if p in fallen_rocks:
            return shape_points
        if p[0] == 0 or p[0] == 8:
            return shape_points

    return mutated_points


def fall(shape_points):
    global fallen_rocks

    mutated_points = mutate_points("V", shape_points)

    for p in mutated_points:
        if p in fallen_rocks or p[1] == 0:
            return False

    return mutated_points


def mutate_points(jet_direction, shape_points):
    new_points = []

    print(jet_direction, shape_points)

    match jet_direction:
        case "<":
            for x, y in shape_points:
                new_points.append((x - 1, y))
            return new_points
        case ">":
            for x, y in shape_points:
                new_points.append((x + 1, y))
            return new_points
        case "V":
            for x, y in shape_points:
                new_points.append((x, y - 1))
            return new_points


if __name__ == "__main__":
    main()
