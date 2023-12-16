import os
import time

test_input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


def get_lines(use_test_data):
    if(use_test_data):
        lines = [list(l) for l in test_input.splitlines()]
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def debug_grid(grid, et):
    os.system('clear')

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if (y, x) in et:
                print(f"\033[93m#\033[0m", end='')
            else:
                print(char, end='')
        print()

def handle_beam(grid, start_pos, start_dir, et):
    stack = [(start_pos, start_dir)]

    while stack:
        # debug_grid(grid, et) # visualize da beam
        pos, dir = stack.pop()
        y, x = pos

        if not (0 <= y < len(grid)) or not (0 <= x < len(grid[y])):
            continue

        if pos in et and dir in et[pos]:
            continue

        if pos not in et:
            et[pos] = []
        et[pos].append(dir)

        char = grid[y][x]
        directions = {
            '.': [dir],
            '|': ['D', 'U'] if dir in ['L', 'R'] else [dir],
            '-': ['L', 'R'] if dir in ['U', 'D'] else [dir],
            '\\': {'D': 'R', 'R': 'D', 'L': 'U', 'U': 'L'}.get(dir, [dir]),
            '/': {'R': 'U', 'D': 'L', 'U': 'R', 'L': 'D'}.get(dir, [dir]),
        }

        for new_dir in directions.get(char, []):
            next_pos = update_pos(pos, new_dir)
            if next_pos != pos:
                stack.append((next_pos, new_dir))
    
def update_pos(pos, dir):
    y, x = pos
    if dir == 'U': y -= 1
    elif dir == 'D': y += 1
    elif dir == 'L': x -= 1
    elif dir == 'R': x += 1
    return (y, x) 

def part_1():
    grid = get_lines(False)
    et = {}

    handle_beam(grid, (0, 0), 'R', et)

    print(f"Part 1 --- {len(et)}")

def part_2():
    grid = get_lines(False)
    energized_count = []

    # top row
    for i in range(len(grid)):
        et = {}
        handle_beam(grid, (0, i), 'D', et)
        energized_count.append(len(et))
    
    # bottom side
    for i in range(len(grid)):
        et = {}
        handle_beam(grid, (len(grid), i), 'U', et)
        energized_count.append(len(et))
    
    # left row
    for i in range(len(grid[0])):
        et = {}
        handle_beam(grid, (i, 0), 'R', et)
        energized_count.append(len(et))

    # right side
    for i in range(len(grid[0])):
        et = {}
        handle_beam(grid, (len(grid), 0), 'L', et)
        energized_count.append(len(et))
    
    print(f"Part 2 --- {max(energized_count)}")

part_1()
part_2()