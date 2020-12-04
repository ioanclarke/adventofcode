fin = open('input.txt')
data = fin.read()
passports = data.split('\n\n')
count = 0
for passport in passports:
    passport = passport.split('\n')
    passport = ' '.join(passport)
    passport = passport.split(' ')
    for i, field in enumerate(passport):
        field = field[:field.find(':')]
        passport[i] = field
    if ('byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and
    'ecl' in passport and 'pid' in passport):
        count += 1

print(count)
