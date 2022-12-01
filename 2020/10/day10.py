joltage_raw = open('puzzle_input.txt', 'r').read().split('\n')

converted_voltage = []
for j in joltage_raw:
    converted_voltage.append(int(j))
converted_voltage.sort()


#Part One
differences = [0, 0, 0]
differences[converted_voltage[0] - 1] += 1

for i, v in enumerate(converted_voltage):
    if(i != len(converted_voltage) - 1):
        difference = converted_voltage[i + 1] - v
        differences[difference - 1] += 1
    else:
        # Last one
        difference = converted_voltage[i] - converted_voltage[i] + 3
        differences[difference - 1] += 1

print(f"Part 1: {differences[0] * differences[2]}")


# Part Two
adapter_paths = {}
adapter_paths[0] = 1
for adapter in converted_voltage:
    amount_of_paths = 0
    for n in (1, 2, 3):
        # print(f"{n} ---> {adapter_paths.get(adapter - n, 0)}")
        amount_of_paths += adapter_paths.get(adapter - n, 0)
    # print(f"Amount of possible paths: {paths_to}")
    adapter_paths[adapter] = amount_of_paths
    # print(f"-------------------------")
    # print(f"{adapter}: {adapter_paths}")

print(f"Part 2: {adapter_paths[converted_voltage[-1]]}")
