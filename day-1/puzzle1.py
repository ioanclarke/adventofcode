fin = open('input.txt')
data = fin.read().split()
for num1 in data:
    for num2 in data:
        for num3 in data:
            if int(num1)+int(num2)+int(num3)==2020:
                print(int(num1)*int(num2)*int(num3))
