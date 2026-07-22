def soma1(l):
    s = 0
    k = 0
    while k < len(l):
        s = s + l[k]
        k += 1
    return s
def soma2(l):
    s = 0
    k = 0
    while k < len(l):
        if l[k] > 0:
            s +=1
        k += 1
    return s
def soma3(l):
    s = 0 
    k = 0
    while k < len(l):
        if l[k] % 2 == 0:
            s += 1
        k += 1
    return s
L = [] #cria uma lista vazia

k = 0
while k < 10:
    n = int(input("Entre um número: "))
    L.append(n)
    k = k + 1
    
print(L)
print('resultados da soma da lista = ',soma1(L))
print('média da lista = ',soma1(L)/10)
print('quantidade de números positivos da lista = ',soma2(L))
print('quantidade de números pares da lista = ', soma3(L))        
            