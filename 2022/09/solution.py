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

# Needed help with this one, had a hard time wrapping my head around how the tail moved and how to handle it when there were more than 2 steps between the head and tail
def follow(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    old_x, old_y = tail

    if (abs(x_diff) == 2) and (abs(y_diff) == 2):
        tail[0] += x_diff//2
        tail[1] += y_diff//2
    else:
        if abs(x_diff) == 2:
            tail[0] += x_diff//2
            tail[1] = head[1]
        elif abs(y_diff) == 2:
            tail[1] += y_diff//2
            tail[0] = head[0]

    new_x, new_y = tail
    return ((new_x != old_x) or (new_y != old_y))

def part_2():
    instructions = get_lines(False)
    touched_spots = {}
    head_x = 0
    head_y = 0
    tail_length = 9
    tail={}

    # init tail
    for i in range(0, tail_length):
        tail[i] = [0, 0]
        if(i == 8): # Add the first tail spot to the touched spots
            touched_spots[str((0,0))] = 1

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
            moved = True

            for i in range(0, tail_length):
                if(i == 0):
                    next_x, next_y = (head_x, head_y)
                else:
                    next_x, next_y = tail[i - 1]

                if moved:
                    moved = follow((next_x, next_y), tail[i])
            
            if moved:
                touched_spots[str(tail[8])] = 1
            
    print(f"Part 2 --- Tail Touched: {len(touched_spots)}")

part_1()
part_2()