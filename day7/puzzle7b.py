def hasNumber(s):
    return any(c.isdigit() for c in s)

def findNumber(s):
    for pos, c in enumerate(s):
        if c.isdigit():
            return pos, c

fin = open('input.txt')
bags = {}
for line in fin:
    bag_name = (line[:line.find('bags') - 1])
    line = line[line.find('contain') + 8:]
    new_bags = {}
    while hasNumber(line):
        numPos, num = findNumber(line)
        new_bag = line[numPos + 2 : line.find('bag') - 1]
        new_bags[new_bag] = num
        line = line[line.find('bag') + 3:]
    bags[bag_name] = new_bags

# for k,v in bags.items():
#     print(k,v)
# for k,v in bags.items():
#     for key, val in bags[k].items():
#         print(k, key, val)

count = 0

def count_bags_in_bag(bag, bags):
    if bags[bag] == {}:
        return 0
    else:
        res = 0
        for subbag, count in bags[bag].items():
            res += int(count) + int(count) * count_bags_in_bag(subbag, bags)
            print(subbag, count)
        return res

print(count_bags_in_bag('shiny gold', bags))
