"""
https://adventofcode.com/2022/day/9
"""

from dataclasses import dataclass

@dataclass
class Point:
    x: int = 0
    y: int = 0

    def getPos(self):
        return (self.x, self.y)

    def move(self, direction):
        match direction:
            case "R": self.x += 1
            case "L": self.x -= 1
            case "U": self.y += 1
            case "D": self.y -= 1


def main():
    moves = []
    with open("./day-09/input.txt") as f:
        moves = [ move.strip().split(" ") for move in f.readlines() ]
    print(f"Problem 1: {p1(moves)}, Problem 2: {p2(moves)}")


def p1(moves: list) -> int:
    h = Point()
    t = Point()
    visited = [[0, 0]]

    for move in moves:
        for _ in range(int(move[1])):
            h.move(move[0])
            t = move_tail(h, t)

            if [t.x, t.y] not in visited:
                visited.append([t.x, t.y])
    
    return len(visited)


def p2(moves: list) -> int:
    rope = [ Point() for _ in range(10) ]
    visited = [[0, 0]]

    for move in moves:
        for _ in range(int(move[1])):
            rope[0].move(move[0])
            # Recursively move tail pos
            for i in range(9):
                t = move_tail(rope[i], rope[i + 1])
                    
            if [t.x, t.y] not in visited:
                visited.append([t.x, t.y])

    return len(visited)


def move_tail(p: Point, t: Point) -> Point:
    offset = [p.x - t.x, p.y - t.y]

    if p.x - 1 <= t.x <= p.x + 1 and p.y - 1 <= t.y <= p.y + 1:
        return t

    # We are in the same row, get direction to move in from offset
    if 0 in offset:
        match offset:
            case [2, 0]: t.move("R")
            case [-2, 0]: t.move("L")
            case [0, 2]: t.move("U")
            case [0, -2]: t.move("D")
    # Diagonal move
    else: 
        if offset[0] > 0 and offset[1] > 0:
            t.move("R")
            t.move("U")
        elif offset[0] < 0 and offset[1] > 0:
            t.move("L")
            t.move("U")
        elif offset[0] > 0 and offset[1] < 0:
            t.move("R")
            t.move("D")
        elif offset[0] < 0 and offset[1] < 0:
            t.move("L")
            t.move("D")

    return t


if __name__ == "__main__":
    main()
