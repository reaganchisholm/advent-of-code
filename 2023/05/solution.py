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
    lines = get_lines(True)
    seeds = lines[0].split(":")[1].strip().split()
    lines = lines[1:] # Remove seeds line
    maps = []

    for l in lines:
        maps.append(l.split(":")[1].strip().splitlines())
    
    for s in seeds:
        print(int(s))

    print(f"Part 1 --- {1}")

part_1()