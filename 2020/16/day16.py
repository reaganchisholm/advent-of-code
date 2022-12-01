import re

puzzle_input = open('puzzle_input.txt').read().split('\n')
puzzle_input_test = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split('\n')

rule_regex = r"^(.+): (\d+)-(\d+) (or) (\d+)-(\d+)"
ticket_regex = r"(\d+),?"
        
def flatten(l):
    return [item for sublist in l for item in sublist]

def remove_duplicates(l):
    return [i for n, i in enumerate(l) if i not in l[:n]]

def parse_input(input):
    rules = []
    tickets = []

    for line in input:
        if(re.match(rule_regex, line)): rules.append(line)
        elif(re.match(ticket_regex, line)): tickets.append(line)
    return rules, tickets

def find_number_ranges(rules):
    ranges = []
    for r in rules:
        matched_rules = re.findall(rule_regex, r)[0]
        num_range_one = list(range(int(matched_rules[1]), (int(matched_rules[2])+1)))
        num_range_two = list(range(int(matched_rules[4]), (int(matched_rules[5])+1)))
        var_one = [*num_range_one, *num_range_two]
        ranges.append(var_one)

    return remove_duplicates(flatten(ranges))

def find_invalid_numbers(num_ranges, tickets):
    invalid_numbers = []
    for t in tickets:
        ticket_numbers = t.split(',')
        for i, tn in enumerate(ticket_numbers):
            if int(tn) not in num_ranges:
                # print(f"Invalid Ticket: {t}")
                invalid_numbers.append(int(tn))
                break
    
    return invalid_numbers

def find_good_tickets(num_ranges, tickets):
    good_tickets = tickets.copy()
    for t in good_tickets:
        ticket_numbers = t.split(',')
        for i, tn in enumerate(ticket_numbers):
            if int(tn) not in num_ranges:
                good_tickets.remove(t)
                break
    
    return good_tickets

# rules, tickets = parse_input(puzzle_input_test)
rules, tickets = parse_input(puzzle_input)
number_ranges = find_number_ranges(rules)
invalid_numbers = find_invalid_numbers(number_ranges, tickets)
good_tickets = find_good_tickets(number_ranges, tickets)

print(f"Part 1: ticket scanning error rate -- {sum(invalid_numbers)}")
print(f"Part 2: -- ")