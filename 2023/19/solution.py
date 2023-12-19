import re

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

    # setup workflows
    for w in workflows:
        key, other = w.split('{')
        other = other.split(',')
        inst = []
        for o in other:
            inst.append(o.replace('}', ''))
        wf[key] = inst
    
    # setup parts
    for part in parts:
        parts = part.replace('}', '').replace('{', '').split(',')
        values = {}
        for a in parts:
            key, value = a.split('=')
            values[key] = value
        p.append(values)
    
    return wf, p

def workflow(wf, key, p):
    if key in ['R', 'A']:
        return key == 'A'

    for inst in wf[key]:
        if '>' in inst or '<' in inst:
            k, comp, num, result = re.findall('(\w+)([<>])(\d+):(\w+)', inst)[0]

            if (comp == '<' and int(p[k]) < int(num)) \
                or (comp == '>' and int(p[k]) > int(num)):
                    return workflow(wf, result, p)
            else:
                continue
        else:
            return workflow(wf, inst, p)

    return False

def part_1():
    workflows, parts = get_lines(False)
    wf, p = prep_data(workflows, parts)
    accepted = []

    for part in p:
        if workflow(wf, 'in', part):
            accepted.append(part)

    total = sum(int(v) for a in accepted for k, v in a.items())
    print(f"Part 1 --- {total}")
                


part_1()