m = []
for i in range(3):
    lin = []
    for j in range(2):
        v = int(input('v: '))
        lin.append(v)
    m.append(lin)

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end = ' ')
    print()
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j]*10, end = ' ')
    print()
