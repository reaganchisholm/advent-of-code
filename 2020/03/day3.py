map_slope = open('puzzle_input.txt', 'r').read().split('\n')
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
totals = [] 

for slope in slopes:
    slope_x = slope[0]
    slope_y = slope[1]
    slope_tree_count = 0
    current_col = slope_x
    current_row = slope_y
    count = 0

    for row in map_slope:
        if(current_row == count):
            if(row[current_col] == '#'):
                slope_tree_count += 1
            current_col += slope_x
            current_row += slope_y
        if(current_col >= 31):
            current_col -= 31
        count += 1

    totals.append(slope_tree_count)

part_two_total = 1
for t in totals:
    part_two_total = part_two_total * t

print(f"Part 1 --- Trees Hit: {totals[1]}")
print(f"Part 2 --- Total Trees Hit: {part_two_total}")