test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def get_priority(letter):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return string.index(letter) + 1

def part_1():
    lines = get_lines(False)
    total = 0

    for line in lines:
        # Split line into two parts, compartment 1, compartment 2
        comp_one, comp_two = line[:len(line)//2], line[len(line)//2:]
        for letter in comp_one:
            # Check if letter is in the 2nd compartment
            if(letter in comp_two):
                # Get the priority of the letter and add it to our total
                total += get_priority(letter)
                break
            else:
                # Letter not found, continue in loop
                continue
    
    print(f"Part 1 --- Score: {total}")

def part_2():
    lines = get_lines(False)
    total = 0

    for i, line in enumerate(lines):
        # Break out of loop if we run out of lines
        if(i+3 > len(lines)):
            break

        # Skip the first line and only check every 4th line
        if(i != 0 and i % 3 != 0):
            continue

        next_line = lines[i+1]
        third_line = lines[i+2]

        for char in line:
            if(char in next_line and char in third_line):
                total += get_priority(char)
                break
            else:
                continue

    print(f"Part 2 --- Score: {total}")

part_1()
part_2()