test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input2.splitlines()
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
            
            touched_spots[(tail_x, tail_y)] = 1

    print(f"Part 1 --- Tail Touched: {len(touched_spots)}")

def part_2():
    instructions = get_lines(True)
    touched_spots = {}
    head_x = 0
    head_y = 0
    tail_length = 9
    tail={}

    # init tail
    for i in range(0, tail_length):
        tail[i] = (0, 0)

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
            for i in range(0, tail_length):
                tail_x, tail_y = tail[i]

                if(i == 0):
                    next_x, next_y = (head_x, head_y)
                else:
                    next_x, next_y = tail[i - 1]

                if tail_x < (next_x - 1): # right
                    tail_x += 1
                    if(tail_y < next_y or tail_y > next_y):
                        tail_y = next_y
                elif tail_x > (next_x + 1): # left
                    tail_x -= 1
                    if(tail_y < next_y or tail_y > next_y):
                        tail_y = next_y
                elif tail_y > (next_y + 1): # up
                    tail_y -= 1
                    if(tail_x < next_x or tail_x > next_x):
                        tail_x = next_x
                elif tail_y < (next_y - 1): # down
                    tail_y += 1
                    if(tail_x < next_x or tail_x > next_x):
                        tail_x = next_x
            
                tail[i] = (tail_x, tail_y)

            touched_spots[tail[8]] = 1
            
    print(f"Part 2 --- Tail Touched: {len(touched_spots)}")

part_1()
part_2()