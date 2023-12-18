import heapq
from collections import defaultdict

test_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

# test_input="""111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991"""

def get_lines(use_test_data):
    if(use_test_data):
        return [list(map(int, list(l))) for l in test_input.splitlines()]
    else :
        with open('input.txt') as f:
            return [list(map(int, list(l))) for l in f.read().splitlines()]

# Directions
R = (1, 0)
L = (-1, 0)
U = (0, -1)
D = (0, 1)

def neighbors(position, width, height, min_run, max_run):
    x, y, direction, run = position
    excluded_directions = [(-direction[0], -direction[1])]
    if run == max_run:
        excluded_directions.append(direction)
    if run < min_run:
        directions = [direction]
    else:
        directions = [R, L, U, D]
    for dir in directions:
        if dir not in excluded_directions:
            yield from new_position(position, dir, width, height, run)

def new_position(position, direction, width, height, current_run):
    x, y, old_direction, run = position
    run = run + 1 if direction == old_direction else 1
    new_x = x + direction[0]
    new_y = y + direction[1]
    if 0 <= new_x < width and 0 <= new_y < height:
        yield new_x, new_y, direction, run

def dijkstra_modified(grid, start, min_run, max_run):
    width = len(grid[0])
    height = len(grid)
    goal = (width - 1, height - 1)
    priority_queue = [(0, start, [])]
    total_heat_loss_map = defaultdict(lambda: float('infinity'))
    while priority_queue:
        heat_loss, position, path = heapq.heappop(priority_queue)
        if (position[0], position[1]) == goal and position[3] >= min_run:
            return heat_loss
        for new_position in neighbors(position, width, height, min_run, max_run):
            new_heat_loss = heat_loss + grid[new_position[1]][new_position[0]]
            if new_heat_loss < total_heat_loss_map[new_position]:
                new_path = path + [position]
                total_heat_loss_map[new_position] = new_heat_loss
                heapq.heappush(priority_queue, (new_heat_loss, new_position, new_path))

def part_1():
    grid = get_lines(False)
    start_position = (0, 0, R, 0)
    end_cost = dijkstra_modified(grid, start_position, 0, 3)
    print(f"Part 1 --- {end_cost}")

def part_2():
    grid = get_lines(False)
    start_position = (0, 0, R, 0)
    end_cost = dijkstra_modified(grid, start_position, 4, 10)
    print(f"Part 2 --- {end_cost}")

part_1()
part_2()