import re

test_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.split("\n")
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split("\n")
            return lines

def part_1():
    lines = get_lines(False)
    match = re.compile(r"Valve (\w+) has flow rate=(\d+); tunnels lead to valves (\w+)(?:, (\w+))?")

part_1()