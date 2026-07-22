def max_Lin(matriz):
    max = []
    for i in range(len(matriz)):
        maior = matriz[i][0]
        for j in range(1,len(matriz[i])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
        max.append(maior)
    return max

def impri(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()



mat = []
linhas = int(input('Total de linhas: '))
colunas = int(input('Total de colunas: '))
for i in range(linhas):
    lin = []
    for j in range(colunas):
        lin.append(int(input(f"Digite valor[{i}][{j}] = ")))
    mat.append(lin)
vetor = max_Lin(mat)
print('Maiores valores: ')
for i in range(len(vetor)):
    print(f'Linha[{i}]: maior = {vetor[i]}')
impri(mat)
