import re

puzzle_input = open('puzzle_input.txt').read().split('\n')
puzzle_input_test = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n')

puzzle_input_test_part_two = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n')

def use_bitmask(mask, value):
	new_value = list(value)
	for i in range(len(mask)):
		if('0' in mask[i] or '1' in mask[i]):
			new_value[i] = mask[i] 
	
	return ''.join(new_value)

def get_leftover_sum(input):
	total_sum = 0
	current_mask = None
	mem = {}

	for i in range(len(input)):
		if 'mask' in input[i]:
			mem_regex = r"(mask)(\s=\s)([X|0|1]+)"
			mem_match = re.findall(mem_regex, input[i])[0]
			current_mask = mem_match[2]
			continue
		else :
			mem_regex = r"(mem\[(\d+?)\])(\s=\s)(\d+)"
			mem_match = re.findall(mem_regex, input[i])[0]
			mem_address = mem_match[1]
			amount = f'{int(mem_match[3]):036b}'

			leftover_bits = use_bitmask(current_mask, amount)
			mem[mem_address] = leftover_bits

	for address in mem:
		total_sum += int(mem[address], 2)

	return total_sum

def use_bitmask_with_floating(mask, address):
	new_address = list(address)
	for i in range(len(mask)):
		if('X' in mask[i] or '1' in mask[i]):
			new_address[i] = mask[i] 
	
	new_address = ''.join(new_address)
	amount_of_floating_chars = 0

	for i in range(len(new_address)):
		if('X' in new_address[i]):
			amount_of_floating_chars += 1

	amount_of_addresses = pow(2, amount_of_floating_chars);
	possibilities = list()

	for i in range(amount_of_addresses):
		possibilities.append(f'{i:0{amount_of_floating_chars}b}')
	
	new_addresses = list()

	for p in possibilities:
		current_num = -1
		updated_address = list(new_address)
		numbers = list(p)

		for i in range(len(updated_address)):
			if('X' in new_address[i]):
				current_num += 1
				updated_address[i] = numbers[current_num]

		new_addresses.append(''.join(updated_address))

	return new_addresses

def get_leftover_sum_part_2(input):
	total_sum = 0
	current_mask = None
	mem = {}

	for i in range(len(input)):
		if 'mask' in input[i]:
			mem_regex = r"(mask)(\s=\s)([X|0|1]+)"
			mem_match = re.findall(mem_regex, input[i])[0]
			current_mask = mem_match[2]
			continue
		else :
			mem_regex = r"(mem\[(\d+?)\])(\s=\s)(\d+)"
			mem_match = re.findall(mem_regex, input[i])[0]
			mem_address = f'{int(mem_match[1]):036b}'
			amount = int(mem_match[3])

			mem_addresses = use_bitmask_with_floating(current_mask, mem_address)

			for i in mem_addresses:
				mem[i] = amount 

	for address in mem:
		total_sum += mem[address]

	return total_sum

part1 = get_leftover_sum(puzzle_input)
part2 = get_leftover_sum_part_2(puzzle_input)

print(f"Part 1 -- Leftover sum: {part1}")
print(f"Part 2 -- Leftover sum: {part2}")
