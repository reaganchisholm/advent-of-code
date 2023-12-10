import numpy as np

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

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
    totals = []

    for l in lines:
        nums = [int(x) for x in l.split()]
        a = np.array(nums)
        total = a[-1]
        while not (a == 0).all():
            a = np.diff(a)
            total += a[-1]
        totals.append(total)

    print(f"Part 1 --- {sum(totals)}")

def part_2():
    lines = get_lines(False)
    totals = []

    for l in lines:
        nums = [int(x) for x in l.split()]
        a = np.array(nums[::-1]) # reverse the array
        total = a[-1]
        while not (a == 0).all():
            a = np.diff(a)
            total += a[-1]
        totals.append(total)

    print(f"Part 2 --- {sum(totals)}")

part_1()
part_2()
