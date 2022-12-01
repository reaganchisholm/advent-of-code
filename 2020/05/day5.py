boarding_pass_raw = open('puzzle_input.txt', 'r').read().split('\n')

def get_seat_ids(boarding_passes):
    seat_ids = []

    for bp in boarding_passes:
        row_min_num = 0
        row_max_num = 128
        row = 0
        col_min_num = 0
        col_max_num = 8
        col = 0

        for i in range(7):
            rows_left = list(range(row_min_num, row_max_num))
            row_mid_point = len(rows_left) // 2
            if(i != 6):
                if bp[i] == 'F':
                    # lower half
                    row_max_num = row_max_num - row_mid_point
                elif bp[i] == 'B':
                    # upper half
                    row_min_num = row_min_num + row_mid_point 
            else:
                if bp[i] == 'F':
                    # lower of the two
                    row = rows_left[0]
                elif bp[i] == 'B':
                    # higher of the two
                    row = rows_left[1]
        for i in range(3):
            cols_left = list(range(col_min_num, col_max_num))
            col_mid_point = len(cols_left) // 2
            if(i != 2):
                if bp[7 + i] == 'L':
                    # lower half
                    col_max_num = col_max_num - col_mid_point
                if bp[7 + i] == 'R':
                    # upper half
                    col_min_num = col_min_num + col_mid_point
            else:
                if bp[7 + i] == 'L':
                    # lower of the two
                    col = cols_left[0]
                elif bp[7 + i] == 'R':
                    # higher of the two
                    col = cols_left[1]

        seat_id = row * 8 + col
        seat_ids.append(seat_id)
        # print(f"{bp}: row {row} col {col} seat ID {round(row * 8 + col)}")

    seat_ids.sort()
    return seat_ids

# ----- Part 1: Testing ----------------------------
# boarding_pass_test = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
# seat_ids = get_seat_ids(boarding_pass_test)
# --------------------------------------------------

def find_my_seat_id(sorted_seat_ids):
    lowest_seat_id = sorted_seat_ids[0]
    highest_seat_id = sorted_seat_ids[-1]
    my_seat_id = None

    for seat_id in range(lowest_seat_id, highest_seat_id):
        if seat_id not in sorted_seat_ids:
            my_seat_id = seat_id
    
    return my_seat_id


seat_ids = get_seat_ids(boarding_pass_raw)
my_seat_id = find_my_seat_id(seat_ids)

print(f"Part 1 -- Highest Seat ID: {seat_ids[-1]}")
print(f"Part 2 -- My Seat ID: {my_seat_id}")