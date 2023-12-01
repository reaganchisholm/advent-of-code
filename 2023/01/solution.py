# test_input = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""
test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
# test_input="""xdglmrpxbz5xpjxzpmvrgsixthreeseven7threebtqfkqp"""

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
    sum = 0

    for l in lines:
        numbers = [s for s in l if s.isdigit()]
        first = numbers[0]
        last = numbers[-1]
        num = first + last
        sum += int(num)

    print(f"Part 1 --- {sum}");

def part_2():
    lines = get_lines(False)
    sum = 0

    for l in lines:
        fixed_line = fix_num_strings(l)
        numbers = [s for s in fixed_line if s.isdigit()]
        first = numbers[0]
        last = numbers[-1]
        num = first + last
        sum += int(num)

    print(f"Part 2 --- {sum}");

def fix_num_strings(string):
    nums = {
        1: 'one', 
        2: 'two', 
        3: 'three', 
        4: 'four', 
        5: 'five', 
        6: 'six', 
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    nums_and_indexes = {}
    
    for key, value in nums.items():
        if value in string:
            index = string.index(value)
            nums_and_indexes[index] = key
            if string.count(value) > 1:
                lindex = string.rindex(value)
                nums_and_indexes[lindex] = key

    ordered = dict(sorted(nums_and_indexes.items()))
    offset = 0

    for key, value in ordered.items():
        string = string[:key + offset] + str(value) + string[key + offset:]
        offset += 1
    
    return string

part_1()
part_2()