def Maior(lista):
    ma = lista [0]
    k = 0
    while k < len(lista):
        if lista[k] > ma:
            ma = lista[k]
        k += 1
    return ma
def Menor(lista):
    me = lista [0]
    k = 0
    while k < len(lista):
        if lista[k] < me:
            me = lista[k]
        k += 1
    return me
    
#...........PROGRAMA PRÍNCIPAL............
L=[]
V=int(input('valor:'))
while V != 0:
    L.append(V)
    V=int(input('valor:'))
print('Maior Valor: ',Maior(L))
print('Menor Valor: ',Menor(L))