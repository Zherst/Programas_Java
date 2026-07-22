def soma(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s

def positivo(l):
    np = 0
    for i in range(len(l)):
        if l[i] > 0:
            np += 1
    return np

def par(l):
    qp = 0
    for i in range(len(l)):
        if l[i] % 2 == 0:
             qp += 1
    return qp

def invertida(l):
    i = []
    for k in range(len(l),0,-1):
        i.append(k)
    return i

l = []
dt = []
r = []
t = int(input('tamanho da lista: '))
for i in range(t):
    n = int(input('número da lista: ' ))
    l.append(n)
    if n % 3 == 0:
        dt.append(n)
    else:
        r.append(n)

        
print('Soma: ', soma(l))
print('média: ', soma(l)/len(l))
print('Quantidade de Positivos: ', positivo(l))
print('Quantidade de Pares: ', par(l))
print('Múltiplos de 3: ', dt)
print('Não múltiplos de 3: ', r)
print('Inversa: ', invertida(l))