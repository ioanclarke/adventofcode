import string
hex_chars = '0123456789abcdef'
eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
digits = '0123456789'

fin = open('input.txt')
data = fin.read()
passports = data.split('\n\n')
count = 0

valid_passports = []
for passport in passports:
    passport = passport.split('\n')
    passport = ' '.join(passport)
    passport = passport.split(' ')

    passport_fields = []
    for field in passport:
        field = field[:field.find(':')]
        passport_fields.append(field)

    if ('byr' in passport_fields and 'iyr' in passport_fields and 'eyr' in passport_fields and 'hgt' in passport_fields and 'hcl' in passport_fields and
    'ecl' in passport_fields and 'pid' in passport_fields):
        valid_passports.append(passport)

print(len(valid_passports))
print(valid_passports)
valid_valids = []
for passport in valid_passports:
    print(passport)
    valid = True
    for entry in passport:
        data = entry[entry.find(':') + 1:]
        if entry.startswith('byr') and not (1920 <= int(data) <= 2002):
            print(entry)
            valid = False
        elif entry.startswith('iyr') and not (2010 <= int(data) <= 2020):
            print(entry)
            valid = False
        elif entry.startswith('eyr') and not (2020 <= int(data) <= 2030):
            print(entry)
            valid = False
        elif entry.startswith('hgt'):
            if data.endswith('cm'):
                if not (150 <= int(data[:-2]) <= 193):
                    print(entry)
                    valid = False
            elif data.endswith('in'):
                if not (59 <= int(data[:-2]) <= 76):
                    print(entry)
                    valid = False
            else:
                print(entry)
                valid = False
        elif entry.startswith('hcl'):
            if data.startswith('#'):
                if len(data) == 7:
                    for char in data[1:]:
                        if char not in hex_chars:
                            print(entry)
                            valid = False
                else:
                    print(entry)
                    valid = False
            else:
                print(entry)
                valid = False
        elif entry.startswith('ecl') and data not in eye_colours:
            print(entry)
            valid = False
        elif entry.startswith('pid'):
            if len(data) == 9:
                for char in data:
                    if char not in digits:
                        print(entry)
                        valid = False
            else:
                print(entry)
                valid = False
    if valid == False:
        print(f'false: {passport}')
        #valid_passports.remove(passport)
    elif valid == True:
        valid_valids.append(passport)
        print(f'true: {passport}')
print(len(valid_passports))
print(valid_passports)
print(len(valid_valids))
