test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

grid="""......
......
......
......
......"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    instructions = get_lines(False)
    touched_spots = {}
    head_x = 0
    head_y = 5
    tail_x = 0
    tail_y = 5

    for ins in instructions:
        d, a = ins.split()

        for i in range(1, int(a) + 1):
            if(d == 'R'): # right
                head_x += 1
            elif(d == 'L'): # left
                head_x -= 1
            elif(d == 'U'): # up
                head_y -= 1
            elif(d == 'D'): # down
                head_y += 1

            # tail handling
            if tail_x < (head_x - 1): # right
                tail_x += 1
                if(tail_y < head_y or tail_y > head_y):
                    tail_y = head_y
            elif tail_x > (head_x + 1): # left
                tail_x -= 1
                if(tail_y < head_y or tail_y > head_y):
                    tail_y = head_y
            elif tail_y > (head_y + 1): # up
                tail_y -= 1
                if(tail_x < head_x or tail_x > head_x):
                    tail_x = head_x
            elif tail_y < (head_y - 1): # down
                tail_y += 1
                if(tail_x < head_x or tail_x > head_x):
                    tail_x = head_x
            
            # print(tail_x, tail_y)
            touched_spots[(tail_x, tail_y)] = 1

    print(f"Part 1 --- Tail Touched: {len(touched_spots)}")

part_1()