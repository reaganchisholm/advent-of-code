from functools import cache

test_input="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

"""
Needed to look at solutions for this one. Brain was not working today.
"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

@cache
def check_line(i, j, cur, ptrn, nums):
    if i == len(ptrn):
        # We have reached the end of the pattern, check if its valid or not
        return (j == len(nums) - 1 and nums[j] == cur) or (j == len(nums) and cur == 0)
    ans = 0
    if ptrn[i] in "#?":
        ans += check_line(i + 1, j, cur + 1, ptrn, nums)
    if ptrn[i] in ".?":
        if cur == 0:
            ans += check_line(i + 1, j, 0, ptrn, nums)
        elif cur > 0 and j < len(nums) and nums[j] == cur:
            ans += check_line(i + 1, j + 1, 0, ptrn, nums)
    return ans

def part_1():
    lines = get_lines(False);
    data = [(x, tuple(map(int, y.split(",")))) for row in lines for x, y in [row.split(" ")]]
    total = 0

    for (ptrn, nums) in data:
        total += check_line(0, 0, 0, ptrn, nums) 

    print(f"Part 1 --- {total}")

def part_2():
    lines = get_lines(False);
    data = [(x, tuple(map(int, y.split(",")))) for row in lines for x, y in [row.split(" ")]]
    unfolded = [("?".join(ptrn for _ in range(5)), tuple(nums * 5)) for ptrn, nums in data]
    total = 0

    for (ptrn, nums) in unfolded:
        total += check_line(0, 0, 0, ptrn, nums) 

    print(f"Part 2 --- {total}")

part_1()
part_2()