directions_raw = open('puzzle_input.txt', 'r').read().split('\n')
directions_test = """F10
N3
F7
R90
F11""".split('\n')

def shift(l, n, d):
    if d == 'left':
        return l[n:] + l[:n]
    elif d == 'right': 
        return l[-n:] + l[:-n]

def p1_simulate_directions(directions):
    current_direction = 90
    n = 0 #North
    e = 0 #East
    s = 0 #South
    w = 0 #West

    for d in directions:
        direction = d[:1]
        amount = int(d[1:])
        # print(f"{direction}{amount}: {current_direction} -- North: {n}, East: {e}, South: {s}, West: {w}")
        if(direction == 'F'):
            if(current_direction == 0 or current_direction == 360):
                if(s != 0):
                    if(s > amount):
                        s = s - amount
                    else:
                        n += amount - s
                        s = 0
                else:
                    n += amount
            elif(current_direction == 90):
                if(w != 0):
                    if(w > amount):
                        w = w - amount
                    else:
                        e += amount - w
                        w = 0
                else:
                    e += amount
            elif(current_direction == 180):
                if(n != 0):
                    if(n > amount):
                        n = n - amount
                    else:
                        s += amount - n
                        n = 0
                else:
                    s += amount
            elif(current_direction == 270):
                if(e != 0):
                    if(e > amount):
                        e = e - amount
                    else:
                        w += amount - e
                        e = 0
                else:
                    w += amount
        elif(direction == 'N'):
            if(s != 0):
                if(s > amount):
                    s = s - amount
                else:
                    n += amount - s
                    s = 0
            else: 
                n += amount
        elif(direction == 'E'):
            if(w != 0):
                if(w > amount):
                    w = w - amount
                else:
                    e += amount - w
                    w = 0
            else: 
                e += amount
        elif(direction == 'S'):
            if(n != 0):
                if(n > amount):
                    n = n - amount
                else:
                    s += amount - n
                    n = 0
            else: 
                s += amount
        elif(direction == 'W'):
            if(e != 0):
                if(e > amount):
                    e = e - amount
                else:
                    w += amount - e
                    e = 0
            else: 
                w += amount
        elif(direction == 'R'):
            current_direction += amount 
            if(current_direction >= 360):
                current_direction = current_direction - 360
        elif(direction == 'L'):
            current_direction -= amount 
            if(current_direction < 0):
                current_direction = 360 + current_direction

    # print(n, e, s, w)
    return (n + s) + (e + w)

def p2_simulate_directions(directions):
    waypoint = [1, 10, 0, 0] # N, E, S, W
    ship = [0, 0, 0, 0] # N, E, S, W

    for d in directions:
        direction = d[:1]
        amount = int(d[1:])

        if direction == 'N':
            if waypoint[2] != 0:
                if waypoint[2] > amount:
                    waypoint[2] -= amount
                else:
                    waypoint[0] +=  amount - waypoint[2]
                    waypoint[2] = 0
            else: 
                waypoint[0] += amount
        elif direction == 'E':
            if waypoint[3] != 0:
                if waypoint[3] > amount:
                    waypoint[3] -= amount
                else:
                    waypoint[1] +=  amount - waypoint[3]
                    waypoint[3] = 0
            else: 
                waypoint[1] += amount
        elif direction == 'S':
            if waypoint[0] != 0:
                if waypoint[0] > amount:
                    waypoint[0] -= amount
                else:
                    waypoint[2] +=  amount - waypoint[0]
                    waypoint[0] = 0
            else: 
                waypoint[2] += amount
        elif direction == 'W':
            if waypoint[1] != 0:
                if waypoint[1] > amount:
                    waypoint[1] -= amount
                else:
                    waypoint[3] += amount - waypoint[1]
                    waypoint[1] = 0
            else: 
                waypoint[3] += amount
        elif direction == 'R':
            shift_amount = round(amount / 90)
            waypoint = shift(waypoint, shift_amount, 'right')
        elif direction == 'L':
            shift_amount = round(amount / 90)
            waypoint = shift(waypoint, shift_amount, 'left')
        elif direction == 'F':
            if sum(ship) == 0:
                ship[0] = waypoint[0] * amount
                ship[1] = waypoint[1] * amount
                ship[2] = waypoint[2] * amount
                ship[3] = waypoint[3] * amount
            else:
                if waypoint[0] == 0:
                    # Going south
                    if ship[0] != 0:
                        if ship[0] > (waypoint[2] * amount):
                            ship[0] = ship[0] - (waypoint[2] * amount)
                        else:
                            ship[2] += (waypoint[2] * amount) - ship[0]
                            ship[0] = 0
                    else: 
                        ship[2] += (waypoint[2] * amount)
                else:
                    # Going north
                    if ship[2] != 0:
                        if ship[2] > (waypoint[0] * amount):
                            ship[2] = ship[2] - (waypoint[0] * amount)
                        else:
                            ship[0] += (waypoint[0] * amount) - ship[2]
                            ship[2] = 0
                    else: 
                        ship[0] += (waypoint[0] * amount)

                if waypoint[1] == 0:
                    # Going west
                    if ship[1] != 0:
                        if ship[1] > (waypoint[3] * amount):
                            ship[1] = ship[1] - (waypoint[3] * amount)
                        else:
                            ship[3] += (waypoint[3] * amount) - ship[1]
                            ship[1] = 0
                    else: 
                        ship[3] += (waypoint[3] * amount)
                else:
                    # Going north
                    if ship[3] != 0:
                        if ship[3] > (waypoint[1] * amount):
                            ship[3] = ship[3] - (waypoint[1] * amount)
                        else:
                            ship[1] += (waypoint[1] * amount) - ship[3]
                            ship[3] = 0
                    else: 
                        ship[1] += (waypoint[1] * amount)

        print(f"{direction}{amount}")
        print(f"WP: {waypoint}")
        print(f"SP: {ship}")
        print("---------------------------")

    return (ship[0] + ship[2]) + (ship[1] + ship[3])

p1_answer_test = p1_simulate_directions(directions_test)
p1_answer = p1_simulate_directions(directions_raw)
p2_answer_test = p2_simulate_directions(directions_test)
p2_answer = p2_simulate_directions(directions_raw)

print(f"Part 1 Test -- Expected: 25, Got: {p1_answer_test}")
print(f"Part 1 -- {p1_answer}") 
print(f"Part 2 Test -- Expected: 286, Got: {p2_answer_test}")
print(f"Part 2 -- {p2_answer}") 
