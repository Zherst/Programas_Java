m = []
for i in range(4):
    lin = []
    for j in range(4):
        if i == j:
            lin.append(1)
        else:
            lin.append(0)
    m.append(lin) #adiciona a linha pronta na matriz
for i in range(len(m)): #loop pelas linhas
    for j in range(len(m[i])): #loop pelas colunas
        print(m[i][j], end = ' ')
    print()
