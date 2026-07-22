def transp(m):
    mt = []
    for i in range(len(m[0])):
        linha = []
        for j in range(len(m)):
            linha.append(m[j][i])
        mt.append(linha)
    return mt
#===========================Programa Principal==============================
matriz = []
nlinhas = int(input('Quantidade de linhas: '))
ncolunas = int(input('Quantidade de colunas: '))
while nlinhas <= 0 or ncolunas <= 0:
    print('Dimensão com Problemas - forneça Valores novamente')
    nlinhas = int(input('Quantidade de linhas: '))
    ncolunas = int(input('Quantidade de colunas: '))
for i in range(nlinhas):
    linha = []
    for j in range(ncolunas):
        valor = int(input('Dígite Valor: '))
        linha.append(valor)
    matriz.append(linha)
for i in range(len(matriz)):
    print(matriz[i])
matrizT = transp(matriz)
for i in range(len(matrizT)):
    print(matrizT[i])