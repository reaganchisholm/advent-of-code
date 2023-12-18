import re

"""
This one is was over my knowledge level. I had to look at solutions to understand what was going on. I did attempt to solve it myself and was able to get test input working but fell apart for full input. 

Some code taken from shared reddit solves and I went through it to better understand as well as watched some videos on shoelace method and pick's theorem. Solutions make sense to me but I wouldn't have come to them on my own.
"""

test_input="""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

def get_lines(use_test_data):
    if(use_test_data):
        return test_input.splitlines()
    else :
        with open('input.txt') as f:
            return f.read().splitlines()

def part_1():
    lines = get_lines(False)
    directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    y, x = (0,0)
    visited = set([(0,0)])

    for line in lines:
        dir, steps, hex = line.split(' ')

        dx, dy = directions[dir]
        for _ in range(int(steps)):
            x += dx
            y += dy
            visited.add((x, y))
    
    # Starting point has to be within the shape, otherwise it won't work. But by using the top left corner of the shape + 1, starting point will be within the shape
    # You could use the bottom right corner - 1 as well, same result
    x, y = min(visited)
    queue = [(x+1, y+1)] 

    while queue:
        x1, y1 = queue.pop()
        for dx, dy in directions.values():
            x2, y2 = x1+dx, y1+dy
            if (x2, y2) not in visited:
                queue.append((x2, y2))
                visited.add((x2, y2))

    print(f"Part 1 --- {len(visited)}")

def part_2():
    lines = get_lines(False)
    regex = r'\(#([a-z0-9]+)([0-3])\)'
    directions = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    y, x = (0,0)
    points = [(0, 0)]
    boundary_area = 0

    for line in lines:
        steps, dir = re.findall(regex, line.split(' ')[2])[0]
        steps = int(steps, 16) # Convert hex to decimal
        dx, dy = directions[int(dir)] # Convert direction to dx, dy
        x += dx * steps
        y += dy * steps
        boundary_area += steps
        points.append((x, y))
    
    # Shoelace formula
    interior_area = 0
    for i in range(len(points)-1):
        (x1, y1), (x2, y2) =  points[i:i+2]
        interior_area += x1*y2 - x2*y1
    interior_area = abs(interior_area) // 2

    # Pick's theorem
    total_area = interior_area + boundary_area//2 + 1

    print(f"Part 2 --- {total_area}")

part_1()
part_2()

