m = []
l = int(input('insira o valor de linhas: '))
c = int(input('insira o valor de colunas: '))

for i in range(l):
    lin = []
    for j in range(c):
        v = int(input('entre um número: '))
        lin.append(v)
    m.append(lin)
    
print('\nMatriz:')
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end = ' ')
    print()
    
    
produto = 1 
for i in range(len(m)):
    for j in range


