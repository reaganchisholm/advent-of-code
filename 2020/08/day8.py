import re, copy

game_instructions = []

with open('puzzle_input.txt') as puzzle_input:
    for line in puzzle_input:
        line = line.replace('\n', '')
        operation = line[:3]
        amount = int(line[4:])
        instruction = [operation, amount, False]
        game_instructions.append(instruction)

def run(instructions):
    copy_of_instructions = copy.deepcopy(instructions)
    current_line = 0 
    accumulator = 0
    game_terminates = False

    while True:
        if(current_line >= len(copy_of_instructions)):
            #If our game gets to one line after our game instruction length, it terminated properly
            game_terminates = True
            break
        
        operation = copy_of_instructions[current_line][0]
        amount = copy_of_instructions[current_line][1]
        instruction_ran_already = copy_of_instructions[current_line][2]

        if(instruction_ran_already):
            # Prevent infinite loop
            break
        else:
            # Mark the line as ran already to prevent infinite loops
            copy_of_instructions[current_line][2] = True

            if(operation == 'nop'):
                current_line += 1
            elif(operation == 'acc'):
                accumulator += amount
                current_line += 1
            elif(operation == 'jmp'):
                current_line += amount
            
    return (accumulator, game_terminates)

def find_all_nop_and_jmp_indexes(instructions):
    all_nop_and_jmps_indexes = []
    for i, line in enumerate(game_instructions):
        operation = line[0]
        if operation == 'nop' or operation == 'jmp':
            all_nop_and_jmps_indexes.append(i)
    return all_nop_and_jmps_indexes

def find_terminating_game(indexes, game_instructions):
    terminated_result = None
    for index in indexes:
        copy_of_game_instructions = copy.deepcopy(game_instructions)
        if(copy_of_game_instructions[index][0] == 'nop'):
            copy_of_game_instructions[index][0] = 'jmp'
            game_result = run(copy_of_game_instructions)
            if(game_result[1] == True):
                terminated_result = game_result 
                break
        if(copy_of_game_instructions[index][0] == 'jmp'):
            copy_of_game_instructions[index][0] = 'nop'
            game_result = run(copy_of_game_instructions)
            if(game_result[1] == True):
                terminated_result = game_result 
                break
    return terminated_result

p1_results = run(game_instructions)

p2_indexes = find_all_nop_and_jmp_indexes(game_instructions)
p2_results = find_terminating_game(p2_indexes, game_instructions)

print(f"Part 1 -- {p1_results[0]}")
print(f"Part 2 -- {p2_results[0]}")