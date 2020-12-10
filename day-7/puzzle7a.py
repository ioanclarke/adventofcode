def hasNumber(s):
    return any(c.isdigit() for c in s)

def findNumber(s):
    for pos, c in enumerate(s):
        if c.isdigit():
            return pos

fin = open('input.txt')
bags = {}
for line in fin:
    bag_name = (line[:line.find('bags') - 1])
    line = line[line.find('contain') + 8:]
    new_bags = []
    while hasNumber(line):
        new_bag = line[findNumber(line) + 2 : line.find('bag') - 1]
        new_bags.append(new_bag)
        line = line[line.find('bag') + 3:]
    bags[bag_name] = new_bags


def bagContainsGold(bag, bags):
    if bags[bag] == []:
        return False
    elif 'shiny gold' in bags[bag]:
        return True
    else:
        res = False
        for subbag in bags[bag]:
            res = res or bagContainsGold(subbag, bags)
        return res

count = 0
for bag in bags:
    if bagContainsGold(bag, bags):
        count += 1

print(count)
