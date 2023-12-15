import re

# test_input="""HASH"""
test_input="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split(",")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split(",")
            return lines

def hash(s):
    val = 0
    for c in s:
        val += ord(c) # ascii value
        val = (val * 17) % 256
    return val

def part_1():
    steps = get_lines(False)
    totals = [hash(s) for s in steps]
    print(f"Part 1 --- {sum(totals)}")

def part_2():
    steps = get_lines(False)
    boxes = {i: {} for i in range(256)}

    for s in steps:
        label, sign, fl = re.match(r'(\w+)([=-])(\d*)?', s).groups()
        box = boxes[hash(label)]
        
        if sign == '-' :
            if label in box: del box[label]
        elif sign == '=' :
            box[label] = int(fl)

    totals = [(b + 1) * (i + 1) * boxes[b][l] for b in boxes for i, l in enumerate(boxes[b])]
    print(f"Part 2 --- {sum(totals)}")

part_1()
part_2()