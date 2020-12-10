fin = open('input.txt')
passes = fin.read().split()

high = 0
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

    high = max(high, rows[0] * 8 + columns[0])

print(high)
