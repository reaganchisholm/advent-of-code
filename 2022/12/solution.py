test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split("\n")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split("\n")
            return lines

def find_shortest_path(graph, start, end):
    start_row = graph[start[1]][start[0]]
    end_row = graph[end[1]][end[0]]
    queue = [(start[1], start[0])]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if (row, col) == end:
            return True
        for row, col in neighbors(graph, row, col, start):
            if(row, col) not in visited:
                queue.append((row, col))
    return visited

def neighbors(graph, row, col, start):
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
    lines = get_lines(True)
    start = (0,0)
    end = (0,0)
    graph = []

    for i, line in enumerate(lines):
        graph_row = []
        for j, char in  enumerate(line):
            if char == "S":
                start = (j,i)
                graph_row.append(elevation.index("a"))
            elif char == "E":
                end = (j,i)
                graph_row.append(elevation.index("z"))
            else:
                graph_row.append(elevation.index(char))
        graph.append(graph_row)
    
    for row in graph:
        print(row)

    paths = find_shortest_path(graph, start, end)
    print(len(paths))
    
part_1()