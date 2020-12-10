fin = open('input.txt')
data = fin.read().split('\n')
count = 0
for line in data:
    if line:
        nums = line[:line.find(' ')]
        lower = nums[:nums.find('-')]
        lower = int(lower) - 1
        upper = nums[nums.find('-') + 1:]
        upper = int(upper) - 1
        letter = line[line.find(' ') + 1: line.find(' ') + 2]
        password = line[line.find(':') + 2:]
        if (password[lower] == letter and password[upper] != letter) or (password[lower] != letter and password[upper] == letter):
            count += 1
print(count)
