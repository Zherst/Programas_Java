def max(m):
    max  = []
    for i in range(len(m)):
        maior = m[i][0]
        for j in range(1,len(m[i])):
            if maior < m[i][j]:
                maior = m[i][j]
        max.append(maior)
    return max

m = []
l = int(input('Números de Linhas: '))
c = int(input('Númenro de Colunas: '))

for i in range(l):
    lin = []
    for j in range(c):
        v = int(input('Válor na matriz:'))
        lin.append(v)
    m.append(lin)

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j],end =' ')
    print()

valor = max(m)
for i in range(len(valor)):
    print(valor[i], end = ' ')