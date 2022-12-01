bus_times = open('puzzle_input.txt').read().split('\n')

bus_test = """939
7,13,x,x,59,x,31,19""".split('\n')

earliest_departure_time = int(bus_times[0])
bus_ids = []

for bus_id in bus_times[1].split(','):
    if bus_id == 'x':
        continue
    else:
        bus_ids.append(int(bus_id))

earliest_times = {}

for count, item in enumerate(bus_ids):
    amount = item
    n = 1 
    while amount < earliest_departure_time:
        if(amount < earliest_departure_time):
            amount = item * n
            n += 1
            earliest_times[item] = amount

answer_bus_id = bus_ids[0]
answer_time_difference = earliest_times[bus_ids[0]] - earliest_departure_time
answer = 0
found_lower = False

for count, bus_id in enumerate(earliest_times):
    if count != 0 and count != len(earliest_times):
        time_difference = earliest_times[bus_id] - earliest_departure_time
        if time_difference < answer_time_difference:
            answer_time_difference = time_difference
            answer_bus_id = bus_id
            answer = time_difference * bus_id 
            found_lower = True

if(found_lower == False):
    answer = answer_time_difference * answer_bus_id

print(f"Part 1: {answer}")

def readFile() -> tuple:
    with open("puzzle_input.txt", "r") as f:
        timestamp = int(f.readline().strip())
        values = f.readline().strip().split(",")
        bus_ids = [{"value": int(values[i]), "index": i} 
            for i in range(len(values))
            if values[i] != "x"]
        return timestamp, bus_ids 

answer_input = readFile()

# Got stuck and found this solution online, still don't fully understand how they got to this solution. Will have to revisit this
def part2(bus_ids: list) -> int:
    minutes, step = 1, 1
    for bus in bus_ids:
        while (minutes + bus["index"]) % bus["value"] != 0:
            # print(f"{minutes} + {bus['index']} % {bus['value']} = {(minutes + bus['index']) % bus['value']}")
            minutes += step
        step *= bus["value"]
    return minutes

p2_answer = part2(answer_input[1])

print(f"Part 2: {p2_answer}")