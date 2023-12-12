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

def find_empty_rows_cols(grid):
    empty_rows = {y for y, row in enumerate(grid) if '#' not in row}
    empty_cols = {x for x in range(len(grid[0])) if all(row[x] != '#' for row in grid)}
    return empty_rows, empty_cols

def manhattan_distance(point1, point2, empty_rows, empty_cols, amount = 1):
    x_distance = abs(point2[0] - point1[0])
    y_distance = abs(point2[1] - point1[1])

    for row in empty_rows:
        if min(point1[1], point2[1]) < row < max(point1[1], point2[1]):
            y_distance += amount

    for col in empty_cols:
        if min(point1[0], point2[0]) < col < max(point1[0], point2[0]):
            x_distance += amount

    return x_distance + y_distance

def part_1():
    lines = get_lines(False)
    grid = [line for line in lines]
    empty_rows, empty_cols = find_empty_rows_cols(grid)
    galaxy_coords = [(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '#'] 
    total_distance = 0

    for i in range(len(galaxy_coords)):
        for j in range(i + 1, len(galaxy_coords)):
            distance = manhattan_distance(galaxy_coords[i], galaxy_coords[j], empty_rows, empty_cols)
            total_distance += distance

    print(f"Part 1 --- {total_distance}")

def part_2():
    lines = get_lines(False)
    grid = [line for line in lines]
    empty_rows, empty_cols = find_empty_rows_cols(grid)
    galaxy_coords = [(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '#'] 

    total_distance = 0

    for i in range(len(galaxy_coords)):
        for j in range(i + 1, len(galaxy_coords)):
            distance = manhattan_distance(galaxy_coords[i], galaxy_coords[j], empty_rows, empty_cols, 999999)
            total_distance += distance

    print(f"Part 2 --- {total_distance}")


part_1()
part_2()