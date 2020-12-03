fin = open('input.txt')
data = fin.read()
data = data.split()
grid = []
for line in data:
    grid.append(list(line))

count = [0,0,0,0,0]
slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
for i in range(len(slopes)):
    pos = [0, 0]
    while pos[0] < 322:
        pos[0] += slopes[i][0]
        pos[1] += slopes[i][1]
        if pos[1] >= 31:
            pos[1] -= 31
        print(pos)
        if pos[0] <= 322:
            if grid[pos[0]][pos[1]] == '#':
                count[i] += 1
print(count)
res = 1
for num in count:
    res *= num
print(res)
