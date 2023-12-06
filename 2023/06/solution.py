from functools import reduce
from time import perf_counter

test_input="""Time:      7  15   30
Distance:  9  40  200"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def format_data(lines):
    times = [int(x) for x in lines[0].split()[1:]]
    distance = [int(x) for x in lines[1].split()[1:]]
    formatted = list(zip(times, distance))
    return formatted

def part_1():
    lines = get_lines(False)
    races = format_data(lines)
    races_amounts = []
    for r in races:
        time, dist = r
        button_held = 0
        possible_wins = []
        while button_held < time:
            boat_dist = button_held * (time - button_held)
            if(boat_dist > dist):
                possible_wins.append(button_held)
            button_held += 1
        races_amounts.append(len(possible_wins))

    total = reduce((lambda x, y: x * y), races_amounts)
    print(f"Part 1 --- {total}")

# Not my initial solution, refactored after learning more about quadratic functions, initial solution was bruteforce (similar to p1)
def part_2():
    lines = get_lines(False)
    time = int(''.join(lines[0].split()[1:]))
    dist = int(''.join(lines[1].split()[1:]))
    low_win, high_win = 0, 0

    for button_held in range(time):
        our_dist = button_held * (time - button_held)
        if our_dist > dist:
            low_win = button_held
            high_win = time - button_held
            break

    total = high_win - low_win + 1
    print(f"Part 2 --- {total}")

part_1()
part_2()