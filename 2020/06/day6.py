group_answers_raw = open('puzzle_input.txt', 'r').read().split('\n\n')

def p1_calc_group_totals(group_answers):
    group_totals = []
    for ga in group_answers:
        group_total = 0
        each_person = ga.split('\n')
        group_answer_check = []
        group_total = 0
        for person in each_person:
            person_answers = list(person)
            for letter in person_answers:
                if letter in group_answer_check:
                    continue
                else:
                    group_answer_check.append(letter)
                    group_total += 1
        
        group_totals.append(group_total)
    
    return group_totals

def p2_calc_group_totals(group_answers):
    group_totals = []
    for ga in group_answers:
        group_total = 0
        each_person = ga.split('\n')
        first_person = each_person[0]
        person_count = len(each_person)
        for char in first_person:
            all_chars = list(ga)
            if all_chars.count(char) == person_count:
                group_total += 1
        
        group_totals.append(group_total)
    
    return group_totals

p1_group_totals = p1_calc_group_totals(group_answers_raw)
p1_group_total_sum = sum(p1_group_totals)

p2_group_totals = p2_calc_group_totals(group_answers_raw)
p2_group_total_sum = sum(p2_group_totals)

print(f"Part 1 -- Group Total Sum: {p1_group_total_sum}")
print(f"Part 2 -- Group Total Sum: {p2_group_total_sum}")
