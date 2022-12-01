import re

puzzle_input = open('puzzle_input.txt', 'r').read().split('\n')
puzzle_input_test = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")

def p1_determineDestination(instructions):
    horizontal = 0
    depth = 0

    for line in instructions:
        instruction_regex = r"(forward|up|down) (\d)"
        instruction_data = re.findall(instruction_regex, line)[0]
        type = instruction_data[0]
        distance = instruction_data[1]

        if(type == 'forward'):
            horizontal += int(distance)
        elif(type == 'up'):
            depth -= int(distance)
        elif(type == 'down'):
            depth += int(distance)

    return horizontal, depth 

def p2_determineDestination(instructions):
    horizontal = 0
    depth = 0
    aim = 0

    for line in instructions:
        instruction_regex = r"(forward|up|down) (\d)"
        instruction_data = re.findall(instruction_regex, line)[0]
        type = instruction_data[0]
        distance = instruction_data[1]

        if(type == 'forward'):
            horizontal += int(distance)
            if(aim != 0):
                depth += (aim * int(distance))
        elif(type == 'up'):
            aim -= int(distance)
        elif(type == 'down'):
            aim += int(distance)

    return horizontal, depth 

part1_answer = p1_determineDestination(puzzle_input)
part2_answer = p2_determineDestination(puzzle_input)

print(f"Part 1 -- {part1_answer} = {part1_answer[0] * part1_answer[1]}");
print(f"Part 2 -- {part2_answer} = {part2_answer[0] * part2_answer[1]}");