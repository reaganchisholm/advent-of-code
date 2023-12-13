test_input="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split("\n\n")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split("\n\n")
            return lines

def part_1():
    patterns = get_lines(False);
    h_mirrors = []
    v_mirrors = []

    for p in patterns:
        rows = p.splitlines()
        columns = [''.join(row[i] for row in rows) for i in range(len(rows[0]))]

        for i, r in enumerate(rows[:-1]):
            if r == rows[i+1]:
                # We found a matching row, now we iterate backwards to check if we hit an edge of the pattern, if so, its a mirror
                is_mirror = True
                offset = 1
                while i - offset >= 0 and i + 1 + offset < len(rows):
                    mirror_start = i+1
                    # print(f"Checking {rows[i - offset]}")
                    # print(f"""         {rows[mirror_start + offset]}""")
                    if rows[i - offset] != rows[mirror_start + offset]:
                        is_mirror = False
                        # print("Not a mirror")
                        break
                    offset += 1
                if is_mirror:
                    h_mirrors.append(i+1)
                    break

        for i, c in enumerate(columns[:-1]):
            if c == columns[i+1]:
                # We found a matching column, now we iterate backwards to check if we hit an edge of the pattern, if so, it's a mirror
                is_mirror = True
                offset = 1
                while i - offset >= 0 and (i + 1 + offset) < len(columns):
                    mirror_start = i + 1
                    # print(f"Checking {columns[i - offset]}")
                    # print(f"""         {columns[mirror_start + offset]}""")
                    if columns[i - offset] != columns[mirror_start + offset]:
                        is_mirror = False
                        break
                    offset += 1
                if is_mirror:
                    v_mirrors.append(i+1)
                    break

    h_total = sum([h * 100 for h in h_mirrors])
    total = h_total + sum(v_mirrors)

    print(f"Part 1 --- {total}")

def part_2():
    patterns = get_lines(True);
    h_mirrors = []
    v_mirrors = []

    for p in patterns:
        rows = p.splitlines()
        columns = [''.join(row[i] for row in rows) for i in range(len(rows[0]))]
        found_mirror = False

        for i, r in enumerate(rows[:-1]):
            if check_if_mirror(r, rows[i+1]) <= 1:
                diff_amount = check_if_mirror(r, rows[i+1]) 
                is_mirror = True
                offset = 1
                while i - offset >= 0 and i + 1 + offset < len(rows):
                    mirror_start = i+1
                    diff = check_if_mirror(rows[i - offset], rows[mirror_start + offset])
                    if diff > 1:
                        is_mirror = False
                        break
                    offset += 1
                    diff_amount += diff
                if is_mirror and diff_amount <= 1:
                    h_mirrors.append(i+1)
                    found_mirror = True
                    break

        if(found_mirror):
            continue
        
        for i, c in enumerate(columns[:-1]):
            if check_if_mirror(c, columns[i+1]) <= 1:
                diff_amount = check_if_mirror(c, columns[i+1])
                is_mirror = True
                offset = 1
                while i - offset >= 0 and (i + 1 + offset) < len(columns):
                    mirror_start = i + 1
                    diff = check_if_mirror(columns[i - offset], columns[mirror_start + offset])
                    if diff > 1:
                        is_mirror = False
                        break
                    offset += 1
                    diff_amount += diff
                if is_mirror and diff_amount <= 1:
                    v_mirrors.append(i+1)
                    break
    
    h_total = sum([h * 100 for h in h_mirrors])
    total = h_total + sum(v_mirrors)

    print(f"Part 2 --- {total}")

def check_if_mirror(line1, line2):
    diff = 0
    for i, c in enumerate(line1):
        if c != line2[i]:
            diff += 1
    return diff
    
part_1()
part_2()