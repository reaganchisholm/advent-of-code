test_input = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

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
    highest = 0
    groups = []
    group = []

    for line in lines:
        if line == "":
            groups.append(group)
            group = []
        else:
            group.append(line)

    groups.append(group)

    for gp in groups:
        total = 0
        for line in gp:
            total += int(line)
        if total > highest:
            highest = total
        
    print(f"Part 1 --- Highest: {highest}");

def part_2():
    lines = get_lines(False)
    highest_three = []
    groups = []
    group = []

    for line in lines:
        if line == "":
            groups.append(group)
            group = []
        else:
            group.append(line)

    groups.append(group)

    for gp in groups:
        total = 0
        for line in gp:
            total += int(line)
        if len(highest_three) < 3:
            highest_three.append(total)
            highest_three.sort()
        else:
            if total > highest_three[0]:
                highest_three[0] = total
                highest_three.sort()
        
    print(f"Part 2 --- Highest: {sum(highest_three)}");

part_1();
part_2();