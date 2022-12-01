import copy

flatten = lambda t: [item for sublist in t for item in sublist]
def pp(LIST):
    for l in LIST:
        print(l)

seats_raw = open('puzzle_input.txt').read()

seats_test = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

seat_array = []
p2_seat_array = []

for l in seats_raw.split('\n'):
    seat_line = []
    for c in l:
        seat_line.append(c)
    seat_array.append(seat_line)
    p2_seat_array.append(seat_line)

copy_of_seats = copy.deepcopy(seat_array)

something_changed = True
amount_of_changes = 0

while something_changed == True:
    if(something_changed == False):
        break
    for line_index, seat_line in enumerate(seat_array):
        for seat_index, seat in enumerate(seat_line):
            if(seat == '.'):
                continue
            adjacent_seats = [
                ["", "", ""],
                ["", "[X]", ""],
                ["", "", ""]
            ]

            if(line_index != 0):
                if(seat_index != 0):
                    adjacent_seats[0][0] = seat_array[line_index - 1][seat_index - 1]
                adjacent_seats[0][1] = seat_array[line_index - 1][seat_index]
                if(seat_index + 1 != len(seat_line)):
                    adjacent_seats[0][2] = seat_array[line_index - 1][seat_index + 1]
            if(seat_index != 0):
                adjacent_seats[1][0] = seat_array[line_index][seat_index - 1]
            if(seat_index + 1 != len(seat_line)):
                adjacent_seats[1][2] = seat_array[line_index][seat_index + 1]
            if(line_index + 1 != len(seat_array)):
                if(seat_index != 0):
                    adjacent_seats[2][0] = seat_array[line_index + 1][seat_index - 1]
                adjacent_seats[2][1] = seat_array[line_index + 1][seat_index]
                if(seat_index + 1 != len(seat_line)):
                    adjacent_seats[2][2] = seat_array[line_index + 1][seat_index + 1]

            flattened = flatten(adjacent_seats)

            if(seat == 'L'):
                if('#' not in flattened):
                    copy_of_seats[line_index][seat_index] = '#'
            elif(seat == '#'):
                if(flattened.count('#') >= 4):
                    copy_of_seats[line_index][seat_index] = 'L'
    amount_of_changes += 1

    # print(f"LAYOUT: {amount_of_changes} ----------------------------")
    # pp(copy_of_seats)

    if(seat_array == copy_of_seats):
        something_changed = False
    else:
        seat_array = copy.deepcopy(copy_of_seats)

occupied_seats = flatten(seat_array).count('#')
print(f"""Part 1 Answer: {occupied_seats}""")

# ------------------------------------------------------------------

p2_seat_test = []

for l in seats_test.split('\n'):
    seat_line = []
    for c in l:
        seat_line.append(c)
    p2_seat_test.append(seat_line)

p2_something_changed = True 
p2_copy_of_seats = copy.deepcopy(p2_seat_test)
p2_amount_of_changes = 0

while p2_something_changed == True:

    if(p2_something_changed == False):
        break

    for p2_line_index, p2_seat_line in enumerate(p2_seat_test):
        for p2_seat_index, p2_seat in enumerate(p2_seat_line):

            if(p2_seat == '.'):
                continue

            p2_adjacent_seats = [
                ["", "", ""],
                ["", "[X]", ""],
                ["", "", ""]
            ]

            if(p2_line_index != 0):
                if(p2_seat_index != 0):
                    top_left_seat = p2_seat_test[p2_line_index - 1][p2_seat_index - 1]
                    if(top_left_seat == '.'):
                        tli = 2
                        while top_left_seat == '.':
                            if(top_left_seat != '.'):
                                break
                            try:
                                if(p2_line_index - tli < 0 or p2_seat_index - tli > len(p2_seat_line)):
                                    break
                                top_left_seat = p2_seat_test[p2_line_index - tli][p2_seat_index - tli]
                                tli += 1
                            except IndexError:
                                break
                    p2_adjacent_seats[0][0] = top_left_seat 

                top_middle_seat = p2_seat_test[p2_line_index - 1][p2_seat_index]
                if(top_middle_seat == '.'):
                    tmi = 2
                    while top_middle_seat == '.':
                        if(top_middle_seat != '.'):
                            break
                        try:
                            if(p2_line_index - tmi < 0):
                                break
                            top_middle_seat = p2_seat_test[p2_line_index - tmi][p2_seat_index]
                            tmi += 1
                        except IndexError:
                            break
                p2_adjacent_seats[0][1] = top_middle_seat

                if(p2_seat_index + 1 != len(p2_seat_line)):
                    top_right_seat = p2_seat_test[p2_line_index - 1][p2_seat_index + 1]
                    if(top_right_seat == '.'):
                        tri = 2
                        while top_right_seat == '.':
                            if(top_right_seat != '.'):
                                break
                            try:
                                if(p2_line_index - tri < 0 or p2_seat_index + tri > len(p2_seat_line)):
                                    break
                                top_right_seat = p2_seat_test[p2_line_index - tri][p2_seat_index + tri]
                                tri += 1
                            except IndexError:
                                break
                            
                    p2_adjacent_seats[0][2] = top_right_seat

            if(p2_seat_index != 0):
                middle_left_seat = p2_seat_test[p2_line_index][p2_seat_index - 1]
                if(middle_left_seat == '.'):
                    mli = 2
                    while middle_left_seat == '.':
                        if(middle_left_seat != '.'):
                            break
                        try:
                            middle_left_seat = p2_seat_test[p2_line_index][p2_seat_index - mli]
                            mli += 1
                        except IndexError:
                            break
                p2_adjacent_seats[1][0] = middle_left_seat

            if(p2_seat_index + 1 != len(p2_seat_line)):
                middle_right_seat = p2_seat_test[p2_line_index][p2_seat_index + 1]
                if(middle_right_seat == '.'):
                    mri = 2
                    while middle_right_seat == '.':
                        if(middle_right_seat != '.'):
                            break
                        try:
                            middle_right_seat = p2_seat_test[p2_line_index][p2_seat_index + mri]
                            mri += 1
                        except IndexError:
                            break
                p2_adjacent_seats[1][2] = middle_right_seat

            if(p2_line_index + 1 != len(p2_seat_test)):
                if(p2_seat_index != 0):
                    bottom_left_seat = p2_seat_test[p2_line_index + 1][p2_seat_index - 1]
                    if(bottom_left_seat == '.'):
                        bli = 2
                        while bottom_left_seat == '.':
                            if(bottom_left_seat != '.'):
                                break
                            try: 
                                bottom_left_seat = p2_seat_test[p2_line_index + bli][p2_seat_index - bli]
                                bli += 1
                            except IndexError:
                                break
                    p2_adjacent_seats[2][0] = bottom_left_seat

                bottom_middle_seat = p2_seat_test[p2_line_index + 1][p2_seat_index]
                if(bottom_middle_seat == '.'):
                    bmi = 2
                    while bottom_middle_seat == '.':
                        if(bottom_middle_seat != '.'):
                            break
                        try: 
                            bottom_middle_seat = p2_seat_test[p2_line_index + bmi][p2_seat_index]
                            bmi += 1
                        except IndexError:
                            break
                p2_adjacent_seats[2][1] = bottom_middle_seat

                if(p2_seat_index + 1 != len(p2_seat_line)):
                    bottom_right_seat = p2_seat_test[p2_line_index + 1][p2_seat_index + 1]
                    if(bottom_right_seat == '.'):
                        bri = 2
                        while bottom_right_seat == '.':
                            if(bottom_right_seat != '.'):
                                break
                            try:
                                bottom_right_seat = p2_seat_test[p2_line_index + bri][p2_seat_index + bri]
                                bri += 1
                            except IndexError:
                                break
                    p2_adjacent_seats[2][2] = bottom_right_seat

            if(p2_amount_of_changes == 4 and p2_line_index == 4 and p2_seat_index == 0):
                print(p2_seat)
                pp(p2_adjacent_seats)
            p2_flattened = flatten(p2_adjacent_seats)

            if(p2_seat == 'L'):
                if('#' not in p2_flattened):
                    p2_copy_of_seats[p2_line_index][p2_seat_index] = '#'
            elif(p2_seat == '#'):
                if(p2_flattened.count('#') >= 5):
                    p2_copy_of_seats[p2_line_index][p2_seat_index] = 'L'

    p2_amount_of_changes += 1

    print(f"LAYOUT: {p2_amount_of_changes} ----------------------------")
    pp(p2_copy_of_seats)

    if(p2_seat_test == p2_copy_of_seats):
        p2_something_changed = False
    else:
        p2_seat_test = copy.deepcopy(p2_copy_of_seats)

p2_occupied_seats = flatten(p2_copy_of_seats).count('#')
print(f"""Part 2 Answer: {p2_occupied_seats}""")
# 2047 close