def matriz(l,c):
    m = []
    for i in range(l):
        lin = []
        for j in range(c):
            lin.append(int(input('Valor na matriz: ')))
        m.append(lin)
    return m
def impri(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end=' ')
        print()

def combinacao(m1,m2):
        for i  in range(len(m1)):
            for j in range(len(m2[i])):
                m1[i].append(m2[i][j])
        return impri(m1)

def transposta(m):
    tran = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            tran[i][j]
            


m1 = []
m2 = []

l = int(input('Número de Linhas: '))
c = int(input('Número de Colunas: '))

print('Matriz A')
m1 = matriz(l,c)
# print('Matriz B')
# m2 = matriz(l,c)

print('Matriz A')
impri(m1)
# print('Matriz B')
# impri(m2)

# combinacao(m1,m2)
print('Tranposta')
transposta(m1)