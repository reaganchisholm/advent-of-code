import re

password_list = open('puzzle_input.txt', 'r').read().split('\n')

total_password_count = 1000
p1_bad_passwords_count = 0
p2_bad_passwords_count = 0

def process_password(password_line):
    # Password format example --- "7-19 c: cckcbwlccccccccczp"
    match = re.findall("(\d+)-(\d+) ([a-z]): ([a-z]+)", password_line)[0]

    if(len(match) > 0):
        minChar = int(match[0])
        maxChar = int(match[1])
        letter = match[2]
        password = match[3]
        return minChar, maxChar, letter, password
    else:
        return print('Unable to process passwords')

for password in password_list:
    minChar, maxChar, letter, password = process_password(password)
    letter_amount = password.count(letter)

    if letter_amount < minChar or letter_amount > maxChar:
        p1_bad_passwords_count += 1

    if password[minChar - 1] is not letter and password[maxChar - 1] is not letter:
        p2_bad_passwords_count += 1
    elif password[minChar - 1] is letter and password[maxChar - 1] is letter:
        p2_bad_passwords_count += 1

print(f"Part 1 -- Bad Passwords Found: {p1_bad_passwords_count}")
print(f"Part 1 -- Answer: {total_password_count - p1_bad_passwords_count}")
print(f"Part 2 -- Bad Passwords Found: {p2_bad_passwords_count}")
print(f"Part 2 -- Answer: {total_password_count - p2_bad_passwords_count}")