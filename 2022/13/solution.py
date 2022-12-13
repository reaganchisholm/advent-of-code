import ast

test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

def get_lines(use_test_data, split_on = "\n\n"):
    if(use_test_data):
        lines = test_input.split(split_on)
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().split(split_on)
            return lines

def check_order(left, right):
    if (isinstance(left, list) and isinstance(right, list)):
        longer_length = len(left) if len(left) > len(right) else len(right)
        result = None
        for i in range(longer_length):
            if(i >= len(left)):
                return True
            elif(i >= len(right)):
                return False
            else:
                result = check_order(left[i], right[i])
                if(result != None):
                    break
        return result
    elif (isinstance(left, int) and isinstance(right, int)):
        if(left > right):
            return False
        elif(left < right):
            return True
        else:
            return None 
    elif(isinstance(left, list) and isinstance(right, int)):
        return check_order(left, [right])
    elif(isinstance(left, int) and isinstance(right, list)):
        return check_order([left], right)

def part_1():
    lines = get_lines(False)
    orders = {}

    for i, line in enumerate(lines):
        left_str, right_str = line.split("\n")
        left = ast.literal_eval(left_str)
        right = ast.literal_eval(right_str)
        order = check_order(left, right)
        orders[i + 1] = order

    total = 0
    for o in orders:
        if(orders[o] == True):
            total += o
    
    print(f"Part 1 --- Sum: {total}")

def part_2():
    lines = get_lines(True, "\n")
    # filter out the empty lines
    lines = list(filter(lambda x: x != "", lines))
    print(lines)
    orders = {}


part_1()
part_2()