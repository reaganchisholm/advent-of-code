test_input="""-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

# test_input="""..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ..."""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    lines = get_lines(True)
    grid = [list(row) for row in lines]
    start = find_start(grid)
    answer = traverse_loop(grid, start)
    print(f"Part 1 --- {answer}")

def find_start(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return i, j
    return None

def get_directions(cell):
    directions = {
        '|': [('N', 'S'), ('S', 'N')],
        '-': [('E', 'W'), ('W', 'E')],
        'L': [('N', 'E'), ('E', 'N')],
        'J': [('N', 'W'), ('W', 'N')],
        '7': [('S', 'W'), ('W', 'S')],
        'F': [('S', 'E'), ('E', 'S')],
        'S': [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]
    }
    return directions.get(cell, [])

def traverse_loop(grid, start):
    max_distance = 0
    visited = set()
    queue = [(start, 0, None)]  # (position, distance, from_direction)

    while queue:
        (x, y), distance, from_direction = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        max_distance = max(max_distance, distance)

        for to_dir, from_dir in get_directions(grid[x][y]):
            if from_direction is None or from_dir != from_direction:
                next_x, next_y = x, y
                if to_dir == 'N': next_x -= 1
                if to_dir == 'S': next_x += 1
                if to_dir == 'E': next_y += 1
                if to_dir == 'W': next_y -= 1
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] != '.':
                    queue.append(((next_x, next_y), distance + 1, to_dir))

    return max_distance

part_1()