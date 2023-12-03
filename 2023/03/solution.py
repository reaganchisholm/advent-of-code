test_input="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

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
    nums = []

    for li, l in enumerate(lines):
        for ci, c in enumerate(l):
            if c.isnumeric() == False and c != '.':
                line_idx = [li - 1, li, li + 1]

                for p in line_idx:
                    if p >= 0:
                        current_line = lines[p]
                        chars = current_line[ci - 1:ci + 2]
                        already_got_num = False
                        for pai, pa in enumerate(chars):
                            if pa.isnumeric() == True and already_got_num == False:
                                c_idx = ci
                                if pai == 0: c_idx -= 1 
                                elif pai == 2: c_idx += 1 
                                full_num = get_full_num(current_line, c_idx)
                                nums.append(full_num)
                                already_got_num = True
                            elif pa.isnumeric() == False and already_got_num == True:
                                already_got_num = False
                            else: continue

    print(f"Part 1 --- {sum(nums)}")

def part_2():
    lines = get_lines(False)
    gear_ratios = []

    for li, l in enumerate(lines):
        for ci, c in enumerate(l):
            if c == '*':
                adj_found = []
                line_idx = [li - 1, li, li + 1]

                for p in line_idx:
                    if p >= 0:
                        current_line = lines[p]
                        chars = current_line[ci - 1:ci + 2]
                        already_got_num = False
                        for pai, pa in enumerate(chars):
                            if pa.isnumeric() == True and already_got_num == False:
                                c_idx = ci
                                if pai == 0: c_idx -= 1 
                                elif pai == 2: c_idx += 1 
                                full_num = get_full_num(current_line, c_idx)
                                adj_found.append(full_num)
                                already_got_num = True
                            elif pa.isnumeric() == False and already_got_num == True:
                                already_got_num = False
                            else: continue
                
                if len(adj_found) == 2:
                    gear_ratios.append(adj_found[0] * adj_found[1])

    print(f"Part 2 --- {sum(gear_ratios)}")
    
def get_full_num(line, ci):
    num = []
    index_check = False
    for index, c in enumerate(line):
        if ci == index:
            index_check = True
        if c.isnumeric() == False:
            if index_check: break;
            else: num = []
        else:
            num.append(c)
    return int(''.join(num))

part_1()
part_2()