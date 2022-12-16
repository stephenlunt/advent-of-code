"""
https://adventofcode.com/2022/day/15
"""

from dataclasses import dataclass

@dataclass
class Sensor:
    x: int
    y: int
    bx: int
    by: int
    r: int


def main():
    sensors = parse()
    beacons = beacon_positions(sensors)
    
    print(f"Beacons not present in: {p1(sensors, beacons, 2000000)} positions")
    print(f"Beacon tuning frequency: {p2(sensors)}")


def parse() -> list:
    sensors = []
    lines = open("./day-15/input.txt").read().splitlines()
    for row in lines:
        coords = row.replace("Sensor at x=", "").replace("closest beacon is at x=", "").replace(" y=", "").split(": ")
        # Sensor coords
        i = coords[0].index(",")
        x, y = int(coords[0][:i]), int(coords[0][i + 1:])
        # Beacon coords
        j = coords[1].index(",")
        bx, by = int(coords[1][:j]), int(coords[1][j + 1:])
        # Calculate radius around beacon
        r = abs(x - bx) + abs(y - by)
        
        sensors.append(Sensor(x, y, bx, by, r))

    return sensors


def beacon_positions(sensors: list[Sensor]) -> set:
    beacons = set()

    for s in sensors:
        beacons.add(complex(s.bx, s.by))

    return beacons


def p1(sensors: list[Sensor], beacons: set, y: int) -> int:
    covered = set()

    for s in sensors:
        y_offset = abs(y - s.y)
        if y_offset <= s.r:
            length = ((s.r * 2) + 1) - (y_offset * 2)
            row_start = s.x - (length // 2)

            for i in range(length):
                pos = complex(row_start + i, y)
                if pos not in beacons:
                    covered.add(pos)

    return len(covered)


def p2(sensors: list[Sensor]) -> int:
    max_y = 4000000 + 1

    for y in range(max_y):        
        start_stops = []

        for s in sensors:
            y_offset = abs(y - s.y)
            if y_offset <= s.r:
                length = ((s.r * 2) + 1) - (y_offset * 2)
                row_start = s.x - (length // 2)
                row_stop = s.x + (length // 2)
                start_stops.append([row_start, row_stop])

        minX = start_stops[0][0]
        maxX = start_stops[0][1]

        count = 0
        while start_stops:
            count += 1
            if count == 1000: # Return when we enter an infinite while loop, hence lists cannot be merged further.
                return ((maxX + 1) * 4000000) + y
            
            # Try merging lists around the min/max values of each start and stop point 
            m, mx = start_stops[0]

            if minX <= m <= maxX and minX <= mx <= maxX:
                start_stops.pop(0)
                continue
            elif m > maxX + 1:
                start_stops.append([m, mx])
                start_stops.pop(0)
                continue
            elif mx < minX - 1:
                start_stops.append([m, mx])
                start_stops.pop(0)
                continue
            
            if m < minX:
                minX = m
            if mx > maxX:
                maxX = mx
                
            start_stops.pop(0)
                

if __name__ == "__main__":
    main()
