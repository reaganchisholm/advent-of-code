test_input = """30373
25512
65332
33549
35390"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    rows = get_lines(False)
    visible_trees = 0

    def check_if_visible(rows, current_height, row, row_max, col, col_max):
        global left_blocked
        global top_blocked
        global right_blocked
        global bottom_blocked

        left_blocked = False
        top_blocked = False
        right_blocked = False
        bottom_blocked = False

        # Tree is on the edge of grid
        if row == 0 or col == 0 or row == row_max or col == col_max:
            return True 

        # left
        for i in range(0, col):
            current_row = rows[row]
            if(int(current_row[i]) >= current_height):
                left_blocked = True
        
        # top 
        for i in range(0, row):
            current_row = rows[i]
            if(int(current_row[col]) >= current_height):
                top_blocked = True
        
        # right
        for i in range(col + 1, col_max + 1):
            current_row = rows[row]
            if(int(current_row[i]) >= current_height):
                right_blocked = True
        
        # bottom
        for i in range(row + 1, row_max + 1):
            current_row = rows[i]
            if(int(current_row[col]) >= current_height):
                bottom_blocked = True
        
        return left_blocked == False or top_blocked == False or right_blocked == False or bottom_blocked == False


    for row, cols in enumerate(rows):
        for col, char in enumerate(cols):
            current_height = int(char)
            is_visible = check_if_visible(rows, current_height, row, len(rows) - 1, col, len(cols) - 1)

            if(is_visible):
                visible_trees += 1
    
    print(f"Part 1 --- Visible Trees: {visible_trees}")

def part_2():
    rows = get_lines(False)
    scenic_scores = []

    def get_scenic_score(rows, current_height, row, row_max, col, col_max):
        global left_blocked
        global top_blocked
        global right_blocked
        global bottom_blocked
        global left_score
        global top_score
        global right_score
        global bottom_score

        left_blocked = False
        top_blocked = False
        right_blocked = False
        bottom_blocked = False

        left_score = 0
        top_score = 0
        right_score = 0
        bottom_score = 0

        # Tree is on the edge of grid
        if row == 0 or col == 0 or row == row_max or col == col_max:
            return 0 

        # left
        for i in range(0, col):
            current_row = rows[row]
            left_score += 1
            if(int(current_row[(col - 1) - i]) >= current_height):
                left_blocked = True
                break
        
        # top 
        for i in range(0, row):
            current_row = rows[(row - 1) - i]
            top_score += 1
            if(int(current_row[col]) >= current_height):
                top_blocked = True
                break
        
        # right
        for i in range(col + 1, col_max + 1):
            current_row = rows[row]
            right_score += 1
            if(int(current_row[i]) >= current_height):
                right_blocked = True
                break
        
        # bottom
        for i in range(row + 1, row_max + 1):
            current_row = rows[i]
            bottom_score += 1
            if(int(current_row[col]) >= current_height):
                bottom_blocked = True
                break
        
        scenic_score = left_score * top_score * right_score * bottom_score
        return scenic_score

    for row, cols in enumerate(rows):
        for col, char in enumerate(cols):
            current_height = int(char)
            scenic_score = get_scenic_score(rows, current_height, row, len(rows) - 1, col, len(cols) - 1)

            if(scenic_score != 0):
                scenic_scores.append(scenic_score)
            
    print(f"Part 2 --- Scenic Scores: {max(scenic_scores)}")

part_1()
part_2()