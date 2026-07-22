m = []
l = int(input('Números de Linhas: '))
c = int(input('Númenro de Colunas: '))

mult = int(input('Número Multiplicador: '))
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
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j]*mult,end =' ')
    print()