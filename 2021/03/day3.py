puzzle_input = open('puzzle_input.txt', 'r').read().split('\n')
puzzle_input_test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")

def part1():
    gamma = ''
    epsilon = ''
    current_num = 0

    while(current_num < len(puzzle_input[0])):
        ones = 0
        zeros = 0

        for line in puzzle_input:
            num = line[current_num]
            if num == '0':
                zeros += 1
            elif num == '1':
                ones += 1

        if(ones > zeros):
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        elif(ones < zeros):
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        
        current_num += 1
    
    return int(gamma,2), int(epsilon,2)

def part2_ogr(lines):
    ogr = lines.copy()
    current_num = 0

    while(True):
        ones = 0
        zeros = 0

        for line in ogr:
            num = line[current_num]
            if num == '0':
                zeros += 1
            elif num == '1':
                ones += 1

        if(ones > zeros):
            ogr = [item for item in ogr if item[current_num] == '1']

        elif(ones < zeros):
            ogr = [item for item in ogr if item[current_num] == '0']
        
        elif(ones == zeros):
            ogr = [item for item in ogr if item[current_num] == '1']
        
        if(len(ogr) == 1):
            break

        current_num += 1
    
    return int(ogr[0], 2)

def part2_c02(lines):
    c02 = lines.copy()
    current_num = 0

    while(True):
        ones = 0
        zeros = 0

        for line in c02:
            num = line[current_num]
            if num == '0':
                zeros += 1
            elif num == '1':
                ones += 1

        if(ones > zeros):
            c02 = [item for item in c02 if item[current_num] == '0']

        elif(ones < zeros):
            c02 = [item for item in c02 if item[current_num] == '1']
        
        elif(ones == zeros):
            c02 = [item for item in c02 if item[current_num] == '0']

        if(len(c02) == 1):
            break
        
        current_num += 1
    
    return int(c02[0], 2)

def part2():
    ogr = part2_ogr(puzzle_input)
    c02 = part2_c02(puzzle_input)

    return ogr * c02

part1_answer = part1()
part2_answer = part2()

print(f"Part 1 -- {part1_answer[0] * part1_answer[1]}");
print(f"Part 2 -- {part2_answer}");