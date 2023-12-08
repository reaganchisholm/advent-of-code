import math

# test_input = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ"""

test_input="""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def get_lines(use_test_data):
    if(use_test_data):
        inst, lines = test_input.split("\n\n")
        lines = lines.splitlines()
        nodes = {}
        start_nodes = []
        for l in lines:
            a, b = l.split(" = ")
            b = b.replace("(", "").replace(")", "").replace(",", "").split(" ")
            nodes[a] = b
            if a[-1] == "A":
                start_nodes.append(a)
        return list(inst), nodes, start_nodes
    else:
        with open('input.txt') as f:
            inst, lines = f.read().split("\n\n")
            lines = lines.splitlines()
            nodes = {}
            start_nodes = []
            for l in lines:
                a, b = l.split(" = ")
                b = b.replace("(", "").replace(")", "").replace(",", "").split(" ")
                nodes[a] = b
                if a[-1] == "A":
                    start_nodes.append(a) 
            return list(inst), nodes, start_nodes

def part_1():
    inst, nodes, _ = get_lines(False)
    current_node = "AAA"
    steps = 0
    
    while current_node != "ZZZ":
        side = inst[steps % len(inst)]
        current_node = nodes[current_node][0 if side == "L" else 1]
        steps += 1
    
    print(f"Part 1 --- {steps}")

def part_2():
    inst, nodes, start_nodes = get_lines(False)
    node_steps = []

    for n in start_nodes:
        steps = 0
        while n[-1] != "Z":
            side = inst[steps % len(inst)]
            n = nodes[n][0 if side == "L" else 1]
            steps += 1
        node_steps.append(steps)
    
    # TIL: Unpacking operator, similar to spread operator in JS, ** is for dictionaries
    print(f"Part 2 --- {math.lcm(*node_steps)}") 

part_1()
part_2()