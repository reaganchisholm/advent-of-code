test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

"""Needed a solution for p2, used that to clean up p1 while I was at it"""

def get_lines(use_test_data):
    if(use_test_data):
        platform = ["".join(c) for c in zip(test_input.splitlines())]
        return platform 
    else :
        with open('input.txt') as f:
            platform = ["".join(c) for c in zip(*f.read().splitlines())]
            return platform

def load(platform):
    return sum(sum(i * (c == "O") for i, c in enumerate(col[::-1], 1)) for col in platform)

def cycle(platform):
    for _ in range(4):
        platform = rotate(tilt(platform))
    return platform

def rotate(platform):
    return ["".join(line) for line in zip(*map(reversed, platform))]

def tilt(platform):
    tilted_platform = list()
    for col in platform:
        tilted = list()
        for group in col.split("#"):
            if group:
                tilted.append("".join(["O"] * group.count("O") + ["."] * group.count(".")))
            else:
                tilted.append("")
        tilted_platform.append("#".join(tilted))
    return tilted_platform

def part_1():
    lines = get_lines(False)
    tilted = tilt(lines)
    answer = load(tilted)
    print(f"Part 1 --- {answer}")

def part_2():
    lines = get_lines(False)
    states = [lines]
    period = transient = t = 0
    target = 1_000_000_000
    
    while True:
        end_cycle = cycle(states[t])
        if end_cycle in states:
            transient = states.index(end_cycle)
            period = t + 1 - states.index(end_cycle)
            break
        states.append(end_cycle)
        t += 1

    answer = load(states[(target - transient) % period + transient])
    print(f"Part 2 --- {answer}")

part_1()
part_2()
