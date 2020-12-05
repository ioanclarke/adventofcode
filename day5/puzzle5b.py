fin = open('input.txt')
passes = fin.read().split()

seatIDs = []
for pas in passes:

    rows = []
    for i in range(128):
        rows.append(i)

    columns = []
    for i in range(8):
        columns.append(i)

    for char in pas[:-3]:
        middle = len(rows) // 2
        if char == 'F':
            rows = rows[:middle]
        else:
            rows = rows[middle:]

    for char in pas[-3:]:
        middle = len(columns) // 2
        if char == 'R':
            columns = columns[middle:]
        else:
            columns = columns[:middle]

    seatIDs.append(rows[0] * 8 + columns[0])

for i in range(128):
    for j in range(8):
        if i*8+j not in seatIDs and i*8+j-1 in seatIDs and i*8+j+1 in seatIDs:
            print(i*8+j)
