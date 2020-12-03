fin = open('input.txt')
data = fin.read().split('\n')
count1 = 0
count2 = 0
for line in data:
    nums = line[:line.find(' ')]
    lower = nums[:nums.find('-')]
    upper = nums[nums.find('-') + 1:]
    letter = line[line.find(' ') + 1: line.find(' ') + 2]
    password = line[line.find(':') + 2:]
    print(f'{lower} {upper} {letter} {password}')
    flag = True
    for char in password:
        if password.count(letter) < int(lower) or password.count(letter) > int(upper):
            flag = False
    if flag == True:
        count1 += 1
    else:
        count2 += 1
print(count1)
print(count2)
