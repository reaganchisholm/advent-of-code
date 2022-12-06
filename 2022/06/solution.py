test_input1="mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test_input2="bvwbjplbgvbhsrlpgdmjqwftvncz"
test_input3="nppdvjthqldpwncqszvftbrmjlhg"
test_input4="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_input5="zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def get_line(use_test_data):
    if(use_test_data):
        return test_input1
    else :
        with open('input.txt') as f:
            line = f.read()
            return line

def part_1():
    line = get_line(False)
    last_char = []
    index = 0

    for i, char in enumerate(line):
        for x in range(i, len(line)):
            cc = line[x]

            if len(last_char) == 4:
                # found 4 chars
                break
            if cc in last_char:
                last_char = []
                break
            else:
                last_char.append(cc)
        if(len(last_char) == 4):
            # found 4 chars
            # print(last_char)
            index = i + 4
            break
    
    print("Part 1 --- First Marker After: ", index)

part_1()