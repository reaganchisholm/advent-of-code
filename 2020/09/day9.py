xmas_transmit_raw = open('puzzle_input.txt', 'r').read().split('\n')
xmas_transmit_test = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split('\n')

def encoding_check(encoded_list, preamble):
    current_line = preamble
    while True:
        num = int(encoded_list[current_line])
        num_failed = True
        previous_numbers = []
        for i in range(preamble):
            previous_numbers.append(encoded_list[(current_line - 1) - i])
        for prev_num in previous_numbers:
            for i in range(preamble - 1):
                test = int(prev_num) + int(previous_numbers[i])
                if test == num:
                    num_failed = False
                    current_line += 1
        if num_failed:
            break

    return encoded_list[current_line]

def find_nums_of_sum(encoded_list, num):
    final_nums = []

    for index, line in enumerate(encoded_list):
        current_nums = [int(line)]
        current_line_index = index
        count = 1

        while True:
            if((current_line_index + count + 1) > len(encoded_list)):
                #Past the end of our list, end loop
                break
            else:
                next_num = int(encoded_list[current_line_index + count])
                current_nums.append(next_num)

                if(sum(current_nums) == int(num)):
                    break
                else:
                    count += 1
        if(sum(current_nums) == int(num)):
            final_nums = current_nums
            break
    
    if(len(final_nums) > 2):
        final_nums.sort()
        final_answer = final_nums[0] + final_nums[-1]
        return final_answer
    else:
        return 'No num found'

test_preamble = 5
preamble = 25
p1_test_answer = encoding_check(xmas_transmit_test, test_preamble)
p1_answer = encoding_check(xmas_transmit_raw, preamble)
p2_test_answer = find_nums_of_sum(xmas_transmit_test, p1_test_answer)
p2_answer = find_nums_of_sum(xmas_transmit_raw, p1_answer)

print(f"Part 1 Test -- Expect: 127 -- Got: {p1_test_answer}")
print(f"Part 1: {p1_answer}")
print(f"Part 2 Test -- Expect: 62 -- Got: {p2_test_answer}")
print(f"Part 2: {p2_answer}")

            



