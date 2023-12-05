# https://adventofcode.com/2023/day/5

from dataclasses import dataclass


@dataclass
class Map:
    src_min: int
    src_max: int
    offset: int


def main():
    p1()
    p2()


def parse():
    with open("./2023/05/input.txt") as f:
        split_data = f.read().split("\n\n")
        return [x.split("\n") for x in split_data]


def p1():
    data = parse()
    seeds = [int(x) for x in data.pop(0)[0].removeprefix("seeds: ").split(" ")]
    print("p1:", find_lowest(data, seeds))


def p2():
    data = parse()
    seeds = [int(x) for x in data.pop(0)[0].removeprefix("seeds: ").split(" ")]
    seed_bounds = []

    for start, length in zip(seeds[::2], seeds[1::2]):
        seed_bounds.append((start, start + length))

    print("p2:", find_lowest_backwards(data, seed_bounds))


def find_lowest(data: list[list[str]], seeds: list[int]):
    maps: list[Map] = []

    for item in data:
        item.pop(0)

        for line in item:
            l = [int(x) for x in line.split(" ")]
            num_map = Map(l[1], l[1] + l[2], l[0] - l[1])
            maps.append(num_map)

        for i, seed in enumerate(seeds):
            for num_map in maps:
                if seed >= num_map.src_min and seed < num_map.src_max:
                    seeds[i] = seed + num_map.offset

        maps = []

    return min(seeds)


def find_lowest_backwards(data: list[list[str]], seed_bounds: list[tuple[int, int]]):
    maps: list[list[Map]] = []
    for item in data[::-1]:
        map: list[Map] = []
        for line in item[1:]:
            l = [int(x) for x in line.split(" ")]
            num_map = Map(l[0], l[0] + l[2], l[1] - l[0])
            map.append(num_map)
        maps.append(map)

    i, loc = 0, 0

    while True:
        for map in maps:
            for num_map in map:
                if loc >= num_map.src_min and loc < num_map.src_max:
                    loc = loc + num_map.offset
                    break

        for min, max in seed_bounds:
            if loc >= min and loc < max:
                return i

        i += 1
        loc = i


if __name__ == "__main__":
    main()
