import re
from functools import reduce

"""
Had to look at solutions for p2, me brain no worky
"""

test_input="""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

def get_lines(use_test_data):
    if(use_test_data):
        workflows, parts = test_input.split('\n\n')
        return workflows.splitlines(), parts.splitlines()
    else :
        with open('input.txt') as f:
            workflows, parts = f.read().split('\n\n')
            return workflows.splitlines(), parts.splitlines()

def prep_data(workflows, parts):
    wf = {}
    p = []

    for w in workflows:
        key, other = w.split('{')
        other = other.split(',')
        inst = []
        for o in other:
            inst.append(o.replace('}', ''))
        wf[key] = inst
    
    for part in parts:
        parts = part.replace('}', '').replace('{', '').split(',')
        values = {}
        for a in parts:
            key, value = a.split('=')
            values[key] = value
        p.append(values)
    
    return wf, p

def workflow(wf, key, p, hit):
    if key in ['R', 'A']:
        return key == 'A'
    else :
        hit.add(key)

    for inst in wf[key]:
        if '>' in inst or '<' in inst:
            k, comp, num, result = re.findall('(\w+)([<>])(\d+):(\w+)', inst)[0]

            if (comp == '<' and int(p[k]) < int(num)) \
                or (comp == '>' and int(p[k]) > int(num)):
                    return workflow(wf, result, p, hit)
            else:
                continue
        else:
            return workflow(wf, inst, p, hit)

    return hit 

def part_1():
    workflows, parts = get_lines(False)
    wf, p = prep_data(workflows, parts)
    accepted = []
    hit = set()

    for part in p:
        if workflow(wf, 'in', part, hit):
            accepted.append(part)

    total = sum(int(v) for a in accepted for k, v in a.items())
    print(f"Part 1 --- {total}")


def part_2():
    wf_lines, parts = get_lines(False)
    workflows, _ = prep_data(wf_lines, parts)
    part = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    parts = []

    queue = [("in", part)]
    while len(queue) > 0:
        wf, part = queue.pop()
        for rule in workflows[wf]:
            if ":" in rule:
                key, comp, num, result = re.findall(r"(\w)([><])(\d+):(\w+)", rule)[0]
                num = int(num)
                cond_part = part.copy()
                
                if comp == '<':
                    cond_part[key] = (cond_part[key][0], num - 1)
                    part[key] = (int(num), part[key][1])
                elif comp == '>':
                    cond_part[key] = (int(num) + 1, cond_part[key][1])
                    part[key] = (part[key][0], int(num))

                if result in ["A", "R"]:
                    if result == "A":
                        parts.append(cond_part.copy())
                else:
                    queue.append((result, cond_part.copy()))
            else:
                if rule in ["A", "R"]:
                    if rule == "A":
                        parts.append(part.copy())
                else:
                    queue.append((rule, part.copy()))

    all_combinations = sum(
        reduce(lambda acc, v: acc * (v[1] - v[0] + 1), part.values(), 1) 
        for part in parts
    )

    print(f"Part 2 --- {all_combinations}")

part_1()
part_2()