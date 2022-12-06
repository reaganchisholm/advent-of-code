test_input="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def get_lines(use_test_data):
    if(use_test_data):
        stack, instructions = test_input.split("\n\n")
        instructions = instructions.splitlines()
        return stack, instructions 
    else :
        with open('input.txt') as f:
            stack, instructions = f.read().split("\n\n")
            instructions = instructions.splitlines()
            return stack, instructions 

def get_instruction(instruction):
    amount = int(instruction.split(" ")[1])
    start_col = int(instruction.split(" ")[3])
    end_col = int(instruction.split(" ")[5])

    return amount, start_col, end_col

def stack_to_array(stack):
    array_stack = []
    lines = stack.splitlines()
    column_count = int(list(lines[-1].replace(" ", ""))[-1])

    # remove last line of column numbers
    lines.pop()

    for line in lines:
        line = line.replace("[", "").replace("]","").split(" ")
        filtered_line = []
        skip_next_n = 0 
        
        for i, char in enumerate(line):
            if(skip_next_n > 0):
                skip_next_n -= 1
                continue
            elif(len(filtered_line) >= column_count):
                # Column is full, let's break out of the loop
                break
            elif char != '':
                filtered_line.append(char)
            elif(char == ''):
                filtered_line.append('')
                skip_next_n = 3

        # loop through each character and add it to the array stack
        for i in range(len(filtered_line)):
            if i >= len(array_stack):
                array_stack.append([])
            if filtered_line[i] != '':
                array_stack[i].append(filtered_line[i])
    
    # Reverse the stacks so its easier to work with
    for stack in array_stack:
        stack.reverse()
            
    return array_stack

def update_stack(stack, amount, start_col, end_col, moveAllTogether=False):
    # get amount from start_col array and remove it
    start_col_array = stack[start_col - 1]
    moved_items = start_col_array[-amount:]
    start_col_array = start_col_array[:-amount]

    # print("Adding {} to {} from {}".format(moved_items, end_col, start_col))

    if(moveAllTogether == False and len(moved_items) > 1):
        moved_items.reverse()

    # add amount to end_col array
    end_col_array = stack[end_col - 1]
    end_col_array.extend(moved_items)

    # update stack
    stack[start_col - 1] = start_col_array
    stack[end_col - 1] = end_col_array

    return stack

def part_1():
    stack, instructions = get_lines(False)
    stack = stack_to_array(stack)
    top_items = []

    for inst in instructions:
        amount, start_col, end_col = get_instruction(inst)
        stack = update_stack(stack, amount, start_col, end_col)

    for s in stack:
        if(len(s) > 0):
            top_items.append(s[-1])

    print(f"Part 1 --- {''.join(top_items)}")

def part_2():
    stack, instructions = get_lines(False)
    stack = stack_to_array(stack)
    top_items = []

    for inst in instructions:
        amount, start_col, end_col = get_instruction(inst)
        stack = update_stack(stack, amount, start_col, end_col, True)

    for s in stack:
        if(len(s) > 0):
            top_items.append(s[-1])

    print(f"Part 2 --- {''.join(top_items)}")

part_1()
part_2()