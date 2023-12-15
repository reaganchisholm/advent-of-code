test_input="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
# test_input="""HASH"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split(",")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split(",")
            return lines

def part_1():
    steps = get_lines(False)
    totals = []

    for s in steps:
        val = 0
        for c in s:
            ascii_v = ord(c)
            val += ascii_v
            val = val * 17
            val = val % 256
        totals.append(val)

    print(f"Part 1 --- {sum(totals)}")

part_1()