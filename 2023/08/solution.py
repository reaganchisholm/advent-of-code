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
        return inst, lines 
    else :
        with open('input.txt') as f:
            inst, lines = f.read().split("\n\n")
            lines = lines.splitlines()
            return inst, lines

def part_1():
    inst, lines = get_lines(False)
    nodes = {}
    inst_i = 0
    steps = 0;
    current_node = "AAA"
    inst = list(inst)

    for l in lines:
        a, b = l.split(" = ")
        b = b.replace("(", "").replace(")", "").replace(",", "").split(" ")
        nodes[a] = b
    
    while current_node != "ZZZ":
        if inst_i >= len(inst):
            inst_i = 0

        side = inst[inst_i]

        if side == "L":
            current_node = nodes[current_node][0]
        elif side == "R":
            current_node = nodes[current_node][1]

        inst_i += 1
        steps += 1
    
    print(f"Part 1 --- {steps}")

def part_2():
    inst, lines = get_lines(False)
    nodes = {}
    inst_i = 0
    steps = 0;
    inst = list(inst)
    starting_nodes = []

    for l in lines:
        a, b = l.split(" = ")
        b = b.replace("(", "").replace(")", "").replace(",", "").split(" ")

        if a[-1] == "A":
            starting_nodes.append(a)

        nodes[a] = b

    while True:
        if inst_i >= len(inst):
            inst_i = 0

        side = inst[inst_i]
        next_nodes = []

        for n in starting_nodes:
            if side == "L":
                next_n = nodes[n][0]
            elif side == "R":
                next_n = nodes[n][1]

            next_nodes.append(next_n)

        starting_nodes = next_nodes
        inst_i += 1
        steps += 1

        print(f"Steps: {steps} --- Nodes: {starting_nodes}\r", end="", flush=True)

        if all(x[-1] == 'Z' for x in starting_nodes):
            break            
    
    print(f"Part 2 --- {steps}")

part_1()
part_2()