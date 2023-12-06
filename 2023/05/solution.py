test_input="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split("\n\n")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split("\n\n")
            return lines

def part_1():
    lines = get_lines(False)
    seeds = [int(s) for s in lines[0].split(":")[1].strip().split()]
    lines = lines[1:] # Remove seeds line
    maps = []
    processed_maps = []
    locations = []

    for l in lines:
        maps.append(l.split(":")[1].strip().splitlines())
    
    for m in maps:
        map_group = []
        for l in m:
            dest, start, rgn = [int(n) for n in l.split()]
            end = start + (rgn - 1)
            diff = abs(dest - start)
            map_group.append([start, end, dest, diff])
        processed_maps.append(map_group)

    for s in seeds:
        for m in processed_maps:
            for g in m:
                if(s >= g[0] and s <= g[1]):
                    diff = s - g[0]
                    s = g[2] + diff
                    break
        locations.append(s)

    print(f"Part 1 --- {min(locations)}")

# This is a very slow brute force solution, but it works :shrug:
def part_2():
    lines = get_lines(False)
    seeds = [int(s) for s in lines[0].split(":")[1].strip().split()]
    lines = lines[1:] # Remove seeds line
    lines = lines[::-1] # Reverse lines
    maps = []
    processed_maps = []
    range_of_seeds = []

    for i in range(0, len(seeds), 2):
        min_max = [seeds[i], seeds[i] + seeds[i+1] - 1]
        range_of_seeds.append(min_max)

    for l in lines:
        maps.append(l.split(":")[1].strip().splitlines())

    for m in maps:
        map_group = []
        for l in m:
            start, dest, rgn = [int(n) for n in l.split()]
            end = start + (rgn - 1)
            diff = abs(dest - start)
            map_group.append([start, end, dest, diff])
        processed_maps.append(map_group)

    location = 0
    lowest_location = 0

    while(True):
        start = location

        for m in processed_maps:
            for g in m:
                if(start >= g[0] and start <= g[1]):
                    diff = start - g[0]
                    start = g[2] + diff
                    break

        for r in range_of_seeds:
            if start >= r[0] and start <= r[1]:
                lowest_location = location; 
                break

        if(lowest_location != 0):
            break
        else:
            location += 1

    print(f"Part 2 --- {lowest_location}")

part_1()
part_2()