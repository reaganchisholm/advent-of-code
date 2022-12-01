puzzle_input = open('puzzle_input.txt', 'r').read().split('\n')

def countChanges(depths):
    increase_count = 0
    decrease_count = 0
    last_number = None

    for d in depths:
        current_number = int(d)
        if(last_number != None): 
            if(current_number > last_number):
                increase_count += 1
            elif(current_number < last_number):
                decrease_count += 1

        last_number = int(d)

    return increase_count, decrease_count

def countSumChanges(depths):
    counter = 0
    increase_count = 0
    decrease_count = 0
    last_sum = None

    while(counter < (len(depths) - 2)):
        current_sum = sum([int(depths[counter]), int(depths[counter+1]), int(depths[counter+2])])

        if(last_sum != None): 
            if(current_sum > last_sum):
                increase_count += 1
            elif(current_sum < last_sum):
                decrease_count += 1

        last_sum = current_sum
        counter += 1

    return increase_count, decrease_count

part1_answer = countChanges(puzzle_input)
part2_answer = countSumChanges(puzzle_input)

print(f"Part 1 -- Increases: {part1_answer[0]}");
print(f"Part 2 -- Sum Increases: {part2_answer[0]}");