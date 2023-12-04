test_input="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    lines = get_lines(False)
    points = []
    for l in lines:
        win_numbers, numbers = l.split(": ")[1].split(" | ")
        win_numbers = set(int(x) for x in win_numbers.split())
        numbers = set(int(x) for x in numbers.split())
        total_wins = len(win_numbers & numbers) # TIL: set intersection operator in python
        card_points = 2 ** (total_wins - 1) if total_wins > 0 else 0
        points.append(card_points)
    print(f"Part 1 --- {sum(points)}")

def part_2():
    lines = get_lines(False)
    scratch_card_count = {}

    for i in range(len(lines)):
        scratch_card_count[i + 1] = 1

    for i, l in enumerate(lines):
        cards_to_check = scratch_card_count[i + 1]
        win_numbers, numbers = l.split(": ")[1].split(" | ")
        win_numbers = set(int(x) for x in win_numbers.split())
        numbers = set(int(x) for x in numbers.split())

        for p in range(cards_to_check):
            matching_nums = len(win_numbers & numbers) # TIL: set intersection operator in python
            for x in range(matching_nums):
                scratch_card_count[i + 1 + x + 1] += 1

    total = sum(scratch_card_count.values())
    print(f"Part 2 --- {total}")

part_1()
part_2()