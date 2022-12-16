import re

test_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

match = re.compile(r"-?\d+")

def get_lines(use_test_data, split_on = "\n"):
    if(use_test_data):
        lines = test_input.split(split_on)
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split(split_on)
            return lines

def part_1():
    lines = get_lines(False)
    beacons = set()
    used_positions = set()
    ROW = 2000000 # use 10 for test input

    for line in lines:
        start_x, start_y, end_x, end_y = map(int, match.findall(line))

        distance = abs(start_x - end_x) + abs(start_y - end_y)
        offset = distance - abs(start_y - ROW)

        if offset < 0:
            continue

        left_x = start_x - offset
        right_x = start_x + offset

        for x in range(left_x, right_x + 1):
            used_positions.add(x)

        if end_y == ROW:
            beacons.add(end_x)
    
    print(f"Part 1 --- Positions: {len(used_positions - beacons)}")

def part_2():
    lines = [list(map(int, match.findall(line))) for line in get_lines(False)]
    MAX_Y = 4000000
    tuning_frequency = None

    for Y in range(MAX_Y + 1):
        visible_intervals = []

        for start_x, start_y, end_x, end_y in lines:
            distance = abs(start_x - end_x) + abs(start_y - end_y)
            offset = distance - abs(start_y - Y)

            if offset < 0:
                continue

            low_x = start_x - offset
            high_x = start_x + offset
                
            visible_intervals.append((low_x, high_x))

        visible_intervals.sort()
        merged_intervals = []

        for low, high in visible_intervals:
            if not merged_intervals:
                merged_intervals.append([low, high])
                continue

            queue_low, queue_high = merged_intervals[-1]

            if low > queue_high + 1:
                merged_intervals.append([low, high])
                continue
                
            merged_intervals[-1][1] = max(queue_high, high)
            
        current_position = 0

        for low, high in merged_intervals:
            if current_position < low:
                tuning_frequency = current_position * 4000000 + Y
                break

            current_position = max(current_position, high + 1)

            if current_position > MAX_Y:
                break
        
        if tuning_frequency:
            break
    
    print(f"Part 2 --- Tuning frequency: {tuning_frequency}")

part_1()
part_2()