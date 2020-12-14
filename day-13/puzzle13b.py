import time
import math
fin = open('input.txt')
data = fin.read().split('\n')
buses = data[1]
buses = buses.split(',')
bus_pos = []

for i, bus in enumerate(buses):
    if bus != 'x':
        bus_pos.append((i, int(bus)))

print(bus_pos)

pos = 0
increment = bus_pos[0][1]
for offset, time in bus_pos[1:]:
    while (pos + offset) % time != 0:
        pos += increment

    increment *= time

print(pos)
# for a, n in bus_pos:
#     print(a,n)

#
# t = 0
# start = time.time()
# while True:
#     flag = True
#     for id, pos in bus_pos:
#         if (t + pos) % id !=0:
#             flag = False
#             break
#     if flag == True:
#         break
#     t += bus_pos[0][0]
# end = time.time()
# print(end-start)
# print(t)
# print()
# max = 0
# for bus in buses:
#     if bus != 'x' and int(bus) > max:
#         max = int(bus)
# print(max)

# t = 100000000000000 - max_pos
# start = time.time()
# while True:
#     flag = True
#     for id, pos in bus_pos:
#         if (t + pos) % id !=0:
#             flag = False
#             break
#     if flag == True:
#         break
#     t += max_bus
# end = time.time()
# print(end-start)
# print(t)
#print(end-start)

# l=[]
# for i, bus in enumerate(buses):
#     if bus != 'x':
#         l.append(int(bus)-i)
# print(l)
# lcm = l[0]
# for i in l[1:]:
#     lcm = lcm*i//math.gcd(lcm,i)
# print(lcm)
