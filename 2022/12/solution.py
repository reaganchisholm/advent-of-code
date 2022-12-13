from colorama import Fore
from colorama import Style

test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def get_color(num):
    color = Fore.WHITE
    if(num > 15):
        color = Fore.RED
    elif(num > 10):
        color = Fore.MAGENTA
    elif(num > 5):
        color = Fore.YELLOW
    elif(num > 0):
        color = Fore.GREEN
    return color

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split("\n")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split("\n")
            return lines

def find_shortest_path(graph, start, end):
    shortest_path = None
    visited = {}
    current = start
    queue = [start]
    visited[start] = None 

    while queue:
        row, col = queue.pop(0)
        current = (row, col)

        if((row, col) == end):
            break

        for row, col in neighbors(graph, row, col):
            if(row, col) not in visited:
                queue.append((row, col))
                visited[(row, col)] = current
    
    # Reconstruct path backwards to find distance
    if current == end:
        path = []
        while visited[current] is not None:
            current = visited[current]
            path.append(current)
        shortest_path = len(path)
    
    return shortest_path

def neighbors(graph, row, col):
    current_height = graph[row][col]
    directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    return [(row, col) for row, col in directions if is_valid_spot(graph, row, col, current_height)]

def is_valid_spot(graph, row, col, current_height):
    if(row >= 0 and row < len(graph) and col >= 0 and col < len(graph[0]) ):
        next_height = graph[row][col]
        is_valid_height = current_height + 1 == next_height or next_height <= current_height
    else:
        is_valid_height = False

    return is_valid_height 

def part_1():
    elevation = "abcdefghijklmnopqrstuvwxyz"
    lines = get_lines(False)
    start = (0,0)
    end = (0,0)
    raw_graph = []

    for i, line in enumerate(lines):
        graph_row = []
        for j, char in  enumerate(line):
            if char == "S":
                start = (i, j)
                graph_row.append(elevation.index("a"))
            elif char == "E":
                end = (i, j)
                graph_row.append(elevation.index("z"))
            else:
                graph_row.append(elevation.index(char))
        raw_graph.append(graph_row)

    # Color visualization of "map"
    # for row in raw_graph:
    #     print("")
    #     for col in row:
    #         print(get_color(col) + str(col).zfill(2) + Style.RESET_ALL, end=" ")
    # print("")
    
    shortest_path = find_shortest_path(raw_graph, start, end)
    print(f"Part 1 --- {shortest_path}")

def part_2():
    elevation = "abcdefghijklmnopqrstuvwxyz"
    starting_points = []
    lines = get_lines(False)
    raw_graph = []
    end = (0,0)

    for i, line in enumerate(lines):
        graph_row = []
        for j, char in  enumerate(line):
            if char == "S":
                start = (i, j)
                starting_points.append((i, j))
                graph_row.append(elevation.index("a"))
            elif char == "E":
                end = (i, j)
                graph_row.append(elevation.index("z"))
            else:
                if(char == "a"):
                    starting_points.append((i, j))
                graph_row.append(elevation.index(char))
        raw_graph.append(graph_row)

    path_lengths = []

    for start in starting_points:
        shortest_path = find_shortest_path(raw_graph, start, end)
        if(shortest_path is not None):
            path_lengths.append(shortest_path)
    
    print(f"Part 2 --- {min(path_lengths)}")

part_1()
part_2()