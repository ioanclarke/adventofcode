#792845136
#389125467
input = '792845136'

node = {}
for i in range(1, len(input) - 1):
    #print(i, input[i])
    node[int(input[i])] = int(input[i+1])

node[int(input[0])] = int(input[1])
node[int(input[-1])] = 10

node[10] = 11
node[1000000] = int(input[0])
for i in range(len(input) + 2, 1000000):
    node[i] = i+1

curr = int(input[0])

for i in range(1000000):
    #print(f'current: {curr}')
    next1 = node[curr]
    next2 = node[node[curr]]
    next3 = node[node[node[curr]]]
    curr_prev = node[curr]
    next3_next = node[next3]
    next3_next_next = node[next3_next]
    #print(f'pick up: {move}')

    dest = curr - 1
    if dest == 0:
        dest = 1000000
    while dest == next1 or dest == next2 or dest == next3:
        dest -= 1
        if dest == 0:
            dest = 1000000
    #print(f'destination: {dest}')

    dest_next = node[dest]
    dest_next_next = node[dest_next]

    node[next1] = next2
    node[next2] = next3
    node[next3] = dest_next
    node[dest_next] = dest_next_next
    node[curr] = next3_next
    node[next3_next] = next3_next_next
    node[dest] = next1

    #curr.next always becomes next3_next
    #next3_next.next doesn't change unless next3_next is dest
    #dest.next always becomes next1
    #dest_next.next doesn't change
    #next1.next always becomes next2
    #next2.next doesn't change
    #next3.next always becomes dest_next

    curr = node[curr]

print(node[1] * node[node[1]])
