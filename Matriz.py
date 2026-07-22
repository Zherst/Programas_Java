def somaD(m):
    s = 0
    nlinhas = len(m)
    ncolunas = len(m[0])
    for i in range(nlinhas):
        for j in range(ncolunas):
            if i == j:
                s = s + m[i][j]
    return s 
def somaAB(m):
    s = 0
    nlinhas = len(m)
    ncolunas = len(m[0])
    for i in range(nlinhas):
        for j in range(ncolunas):
            if i > j:
                s = s + m[i][j]
    return s
def triang(m):
    nlinhas = len(m)
    ncolunas = len(m[0])
    for i in range(nlinhas):
        for j in range(ncolunas):
            if i != j:
                m[i][j] = 0
    return m
#====================programa principal==============================
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        if i < j:
            linha.append(2*i + 7*j - 2)
        elif i == j:
            linha.append(3*i**2 + 1)
        else: 
            linha.append(4*i**3 + 5*j**2 + 1)
    matriz.append(linha)

print('Matriz Original')
for i in range(10):
    print(matriz[i])
    
print('soma dos elementos da diagonal principal: ', somaD(matriz))
print('A soma dos elementos abaixo da diagonal principal: ', somaAB(matriz))

mtriang = triang(matriz)

print('Matriz triangular')
for i in range(10):
    print(mtriang[i])
    


