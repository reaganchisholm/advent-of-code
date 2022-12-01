puzzle_input = [10,16,6,0,1,17]
puzzle_input_test = [0,3,6]

def play_game(input, number_of_turns):
    record = {}
    current_number = input[0]
    count = 1

    for num in input:
        # print(num)
        record[num] = {
            "spoken": 1,
            "turns": [count] 
        }
        count += 1
    
    def add_record(number, turn):
        if number in record:
            record[number]["spoken"] += 1
            record[number]["turns"].append(turn)
        else :
            record[number] = {
                "spoken": 1,
                "turns": [turn]
            }

    while count < (number_of_turns + 1):
        if current_number in record:
            if record[current_number]["spoken"] == 1:
                current_number = 0
                add_record(current_number, count)
                
            else: 
                distance = (count - 1) - int(record[current_number]["turns"][-2])
                current_number = distance
                add_record(current_number, count)
        else:
            add_record(current_number, count)

        count += 1

    return current_number

# part1_test = play_game(puzzle_input_test, 2020)
# print(part1_test)

part1 = play_game(puzzle_input, 2020)
print(f"Part 1: 2020th number spoken -- {part1}")

part2 = play_game(puzzle_input, 30000000)
print(f"Part 2: 30000000th number spoken -- {part2}")
