# test_input="""-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF"""

# test_input="""..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ..."""

# test_input="""...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ..........."""

test_input=""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

"""
Needed to look at solutions for this one, will have to come back to it to understand better
"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    grid = get_lines(False)
    width, height = len(grid[0]), len(grid)
    
    def get_adjacent(x, y, tile):
        directions = []
        if tile in '-J7S':
            directions.append((x, y - 1))
        if tile in '-FLS':
            directions.append((x, y + 1))
        if tile in '|F7S':
            directions.append((x + 1, y))
        if tile in '|LJS':
            directions.append((x - 1, y))
        return directions

    graph, visited, queue = {}, set(), set()
    for x in range(height):
        for y in range(width):
            tile = grid[x][y]
            graph[(x, y)] = get_adjacent(x, y, tile)
            if tile == 'S':
                visited.add((x, y))
                queue.add((x, y))

    steps = -1
    while queue:
        next_queue = set()
        for x1, y1 in queue:
            for x2, y2 in graph[(x1, y1)]:
                if (x2, y2) not in visited and (x1, y1) in graph.get((x2, y2), []):
                    next_queue.add((x2, y2))
                    visited.add((x2, y2))
        queue = next_queue
        steps += 1

    print(f"Part 1 --- {steps}")

def part_2():
    def build_graph(grid):
        graph = {}
        start = None
        for x, line in enumerate(grid):
            for y, tile in enumerate(line):
                adjacent = get_adjacent_tiles(x, y, tile)
                if tile == 'S':
                    start = (x, y)
                graph[(x, y)] = adjacent
        return graph, start

    def get_adjacent_tiles(x, y, tile):
        adjacent = []
        if tile in '-J7S':
            adjacent.append((x, y - 1))
        if tile in '-FLS':
            adjacent.append((x, y + 1))
        if tile in '|F7S':
            adjacent.append((x + 1, y))
        if tile in '|LJS':
            adjacent.append((x - 1, y))
        return adjacent

    def traverse_graph(graph, start):
        pipes = set()
        tile_q = {start}
        while tile_q:
            nxt = set()
            for x1, y1 in tile_q:
                for x2, y2 in graph[(x1, y1)]:
                    if (x1, y1) not in graph.get((x2, y2), []):
                        continue
                    pipe = (*sorted((x1, x2)), *sorted((y1, y2)))
                    if pipe not in pipes:
                        pipes.add(pipe)
                        nxt.add((x2, y2))
            tile_q = nxt
        return pipes

    def calculate_corners(grid, pipes):
        m, n = len(grid), len(grid[0])
        visited = set()
        corner_q = [(0, 0)]

        while corner_q:
            x, y = corner_q.pop()
            requirements = (x > 0, y < n, x < m, y > 0)
            adjacent = ((x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1))
            tile_pairs = ((x - 1, x - 1, y - 1, y),
                          (x - 1, x, y, y),
                          (x, x, y - 1, y),
                          (x - 1, x, y - 1, y - 1))
            for req, corner, tile_pair in zip(requirements, adjacent, tile_pairs):
                if req and corner not in visited and tile_pair not in pipes:
                    visited.add(corner)
                    corner_q.append(corner)

        total = m * n - len(pipes)
        for i in range(m):
            for j in range(n):
                corners = ((i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1))
                if all(c in visited for c in corners):
                    total -= 1

        return total

    grid = get_lines(False)
    graph, start = build_graph(grid)
    pipes = traverse_graph(graph, start)
    total = calculate_corners(grid, pipes)
    
    print(f"Part 2 --- {total}")

part_1()
part_2()