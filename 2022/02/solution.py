test_input = """A Y
B X
C Z
"""

# Win = 6
# Draw = 3
# Lose = 0

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
    result = 0;

    def determine_outcome(op_move, my_move):
        # A | X = Rock - 1pt
        # B | Y = Paper - 2pt
        # C | Z = Scissors - 3pt

        shape_value = 0;

        if(my_move == 'X'): 
            shape_value += 1
        if(my_move == 'Y'): 
            shape_value += 2
        if(my_move == 'Z'): 
            shape_value += 3

        if(op_move == 'A'):
            if(my_move == 'X'):
                return 3 + shape_value
            elif(my_move == 'Y'):
                return 6 + shape_value
            elif(my_move == 'Z'):
                return 0 + shape_value
        elif(op_move == 'B'):
            if(my_move == 'Y'):
                return 3 + shape_value
            elif(my_move == 'Z'):
                return 6 + shape_value
            elif(my_move == 'X'):
                return 0 + shape_value
        elif(op_move == 'C'):
            if(my_move == 'Z'):
                return 3 + shape_value
            elif(my_move == 'X'):
                return 6 + shape_value
            elif(my_move == 'Y'):
                return 0 + shape_value
        return 'Unknown move'

    for line in lines:
        letters = line.split(" ")
        op_move = letters[0]
        my_move = letters[1]
        result += determine_outcome(op_move, my_move)
    
    print(f"Part 1 --- Score: {result}")

def part_2():
    lines = get_lines(False)
    result = 0

    def determine_outcome(op_move, my_move):
        shape_value = 0

        # A = Rock - 1pt
        # B = Paper - 2pt
        # C = Scissors - 3pt

        # X = Lose
        # Y = Draw
        # Z = Win

        if(my_move == 'X'): 
            # Need to LOSE the game
            if(op_move == 'A'):
                shape_value += 3
            elif(op_move == 'B'):
                shape_value += 1
            elif(op_move == 'C'):
                shape_value += 2
            return 0 + shape_value
        if(my_move == 'Y'): 
            # Need to DRAW the game
            if(op_move == 'A'):
                shape_value += 1
            elif(op_move == 'B'):
                shape_value += 2
            elif(op_move == 'C'):
                shape_value += 3
            return 3 + shape_value
        if(my_move == 'Z'): 
            # Need to WIN the game
            if(op_move == 'A'):
                shape_value += 2
            elif(op_move == 'B'):
                shape_value += 3
            elif(op_move == 'C'):
                shape_value += 1
            return 6 + shape_value
        return 'Unknown move'

    for line in lines:
        letters = line.split(" ")
        op_move = letters[0]
        my_move = letters[1]
        result += determine_outcome(op_move, my_move)
    
    print(f"Part 2 --- Score: {result}")

part_1()
part_2()