test_input="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    lines = get_lines(False)
    grid = build_grid(lines)
    empty_rows, empty_cols = find_empty_rows_cols(grid)
    galaxy_coords = get_galaxy_coords(grid)

    total_distance = 0

    for i in range(len(galaxy_coords)):
        for j in range(i + 1, len(galaxy_coords)):
            distance = manhattan_distance_p1(galaxy_coords[i], galaxy_coords[j], empty_rows, empty_cols)
            total_distance += distance

    print(f"Part 1 --- {total_distance}")

def part_2():
    lines = get_lines(False)
    grid = build_grid(lines)
    empty_rows, empty_cols = find_empty_rows_cols(grid)
    galaxy_coords = get_galaxy_coords(grid)

    total_distance = 0

    for i in range(len(galaxy_coords)):
        for j in range(i + 1, len(galaxy_coords)):
            distance = manhattan_distance_p2(galaxy_coords[i], galaxy_coords[j], empty_rows, empty_cols)
            total_distance += distance

    print(f"Part 2 --- {total_distance}")

def build_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid

def get_galaxy_coords(grid):
    galaxy_coords = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if(grid[y][x] == '#'):
                galaxy_coords.append((x,y))

    return galaxy_coords 

def find_empty_rows_cols(grid):
    empty_rows = set(range(len(grid)))
    empty_cols = set(range(len(grid[0])))

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                if y in empty_rows:
                    empty_rows.remove(y)
                if x in empty_cols:
                    empty_cols.remove(x)

    return empty_rows, empty_cols

def manhattan_distance_p1(point1, point2, empty_rows, empty_cols):
    x_distance = abs(point2[0] - point1[0])
    y_distance = abs(point2[1] - point1[1])

    for row in empty_rows:
        if min(point1[1], point2[1]) < row < max(point1[1], point2[1]):
            y_distance += 1

    for col in empty_cols:
        if min(point1[0], point2[0]) < col < max(point1[0], point2[0]):
            x_distance += 1

    return x_distance + y_distance

def manhattan_distance_p2(point1, point2, empty_rows, empty_cols):
    x_distance = abs(point2[0] - point1[0])
    y_distance = abs(point2[1] - point1[1])

    for row in empty_rows:
        if min(point1[1], point2[1]) < row < max(point1[1], point2[1]):
            y_distance += 999999

    for col in empty_cols:
        if min(point1[0], point2[0]) < col < max(point1[0], point2[0]):
            x_distance += 999999

    return x_distance + y_distance

part_1()
part_2()