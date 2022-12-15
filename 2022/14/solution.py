# Brain was not working for this one, watched this video for help: youtube.com/watch?v=Uf_IF_3RbKw

test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

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
    abyss = 0
    b = set()
    t = 0

    for line in lines:
        x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    b.add(x + y * 1j)
                    abyss = max(abyss, y + 1)

    while True:
        s = 500
        while True:
            if s.imag >= abyss:
                break
            if s + 1j not in b:
                s += 1j
                continue
            if s + 1j - 1 not in b:
                s += 1j - 1
                continue
            if s + 1j + 1 not in b:
                s += 1j + 1
                continue   
            b.add(s)
            t += 1
            break
        if(s.imag >= abyss):
            break

    print(f"Part 1 --- Sand: {t}")

def part_2():
    lines = get_lines(False)
    abyss = 0
    b = set()
    t = 0

    for line in lines:
        x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])

            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    b.add(x + y * 1j)
                    abyss = max(abyss, y + 1)

    while 500 not in b:
        s = 500
        while True:
            if s.imag >= abyss:
                break
            if s + 1j not in b:
                s += 1j
                continue
            if s + 1j - 1 not in b:
                s += 1j - 1
                continue
            if s + 1j + 1 not in b:
                s += 1j + 1
                continue   
            break
        b.add(s)
        t += 1

    print(f"Part 2 --- Sand: {t}")
            
part_1()
part_2()