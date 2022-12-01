import re

passports_raw = open('puzzle_input.txt', 'r').read().split('\n\n')

def setup_passports(passports_string):
    restructured_passports = []

    for passport_string in passports_string:
        passport = create_passport(passport_string)
        restructured_passports.append(passport)

    return restructured_passports

def create_passport(passport_string):
    deconstructed_passport = re.findall("([a-z]{3}):(\S+)", passport_string)
    passport = { "byr": None, "iyr": None, "eyr": None, "hgt": None, "hcl": None, "ecl": None, "pid": None, "cid": None }

    for dp in deconstructed_passport:
        passport[dp[0]] = dp[1]

    return passport

def verify_passports_p1(passports):
    amount_of_verified_passports = 0
    for passport in passports:
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        passport_verified = True
        for field, value in passport.items():
            if(field in required_fields):
                if(value == None):
                    passport_verified = False
        if(passport_verified):
            amount_of_verified_passports += 1

    return amount_of_verified_passports

def verify_passports_p2(passports):
    amount_of_verified_passports = 0
    for passport in passports:
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        passport_verified = True
        for field, value in passport.items():
            if(field in required_fields):
                if(value == None):
                    passport_verified = False
                elif(field == 'byr'):
                    if(len(str(value)) != 4 or int(value) < 1920 or int(value) > 2002):
                        passport_verified = False
                elif(field == 'iyr'):
                    if(len(str(value)) != 4 or int(value) < 2010 or int(value) > 2020):
                        passport_verified = False
                elif(field == 'eyr'):
                    if(len(str(value)) != 4 or int(value) < 2020 or int(value) > 2030):
                        passport_verified = False
                elif(field == 'hgt'):
                    match = re.findall('(\d+)(in|cm)', value)
                    if(len(match) == 1):
                        height = int(match[0][0])
                        height_type = match[0][1]
                        if(height_type == 'cm' and (height < 150 or height > 193)):
                            passport_verified = False
                        elif(height_type == 'in' and (height < 59 or height > 76)):
                            passport_verified = False
                    else:
                        passport_verified = False
                elif(field == 'hcl'):
                    pattern = '^#[a-f0-9]{6}$' 
                    if re.match(pattern, value) is None:
                        passport_verified = False
                elif(field == 'ecl'):
                    pattern = '^(amb|blu|brn|gry|grn|hzl|oth)$' 
                    if re.match(pattern, value) is None:
                        passport_verified = False
                elif(field == 'pid'):
                    pattern = '^\d{9}$' 
                    if re.match(pattern, value) is None:
                        passport_verified = False
        if(passport_verified):
            amount_of_verified_passports += 1

    return amount_of_verified_passports

#----------------------------------

passports = setup_passports(passports_raw)
verified_passports_p1 = verify_passports_p1(passports)
verified_passports_p2 = verify_passports_p2(passports)

print(f"Part 1 -- Verified Passports: {verified_passports_p1}")
print(f"Part 2 -- Verified Passports: {verified_passports_p2}")