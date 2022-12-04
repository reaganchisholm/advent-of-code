test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
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
    total = 0

    for line in lines:
        elf_one, elf_two = line.split(",")
        elf_one = elf_one.split("-")
        elf_two = elf_two.split("-")
        elf_one_range = range(int(elf_one[0]), int(elf_one[1]) + 1)
        elf_two_range = range(int(elf_two[0]), int(elf_two[1]) + 1)

        if(len(set(elf_one_range).intersection(elf_two_range)) == len(elf_one_range)):
            total += 1
        elif(len(set(elf_two_range).intersection(elf_one_range)) == len(elf_two_range)):
            total += 1
        else:
            continue
    
    print(f"Part 1 --- Total: {total}")

def part_2():
    lines = get_lines(False)
    total = 0

    for line in lines:
        elf_one, elf_two = line.split(",")
        elf_one = elf_one.split("-")
        elf_two = elf_two.split("-")
        elf_one_range = range(int(elf_one[0]), int(elf_one[1]) + 1)
        elf_two_range = range(int(elf_two[0]), int(elf_two[1]) + 1)

        if(len(set(elf_one_range).intersection(elf_two_range)) > 0):
            total += 1
        elif(len(set(elf_two_range).intersection(elf_one_range)) > 0):
            total += 1
        else:
            continue
    
    print(f"Part 2 --- Total: {total}")

part_1()
part_2()