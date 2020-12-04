fin = open('input.txt')
data = fin.read()
data = data.split()
grid = []
for line in data:
    grid.append(list(line))

count = 0
pos = [0, 0]
while pos[0] < 322:
    pos[0] += 1
    pos[1] += 3
    if pos[1] >= 31:
        pos[1] -= 31
    print(pos)
    if grid[pos[0]][pos[1]] == '#':
        count += 1
print(count)
