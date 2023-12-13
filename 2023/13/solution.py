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
                    if mirror_start+offset >= len(rows):
                        break
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
                    if mirror_start + offset >= len(columns):
                        break
                if is_mirror:
                    v_mirrors.append(i+1)
                    break

    h_total = sum([h * 100 for h in h_mirrors])
    total = h_total + sum(v_mirrors)

    print(f"Part 1 --- {total}")

def part_2():
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
                    if mirror_start+offset >= len(rows):
                        break
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
                        # Can we fix a "smudge" by switching a # to a . or vice versa?
                        is_mirror = False
                        break
                    offset += 1
                    if mirror_start + offset >= len(columns):
                        break
                if is_mirror:
                    v_mirrors.append(i+1)
                    break

    h_total = sum([h * 100 for h in h_mirrors])
    total = h_total + sum(v_mirrors)

    print(f"Part 2 --- {total}")
    
part_1()
part_2()