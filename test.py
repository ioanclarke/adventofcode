l = [1,2,3,4,5,6,7,8,9,10]
for i, num in enumerate(l):
    print(i, num)
    if num%2==0:
        l.remove(num)
print(l)
