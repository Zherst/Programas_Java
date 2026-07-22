m = []
n = 0
for i in range(3):
    lin = []
    for j in range(3):
        n += 1
        lin.append(n)
    m.append(lin)
pd = 1
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j],end=' ')
        if i == j:
            pd *= m[i][j]
    print()
print('Produto da Diagonal: ', pd)