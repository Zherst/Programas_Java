def invertida(l,k):
    iv = []
    while k > 0:
        iv.append(l[k-1])
        k -= 1
    return print('Inversa da Lista: ', iv)        

def lista(l,k):
    p = []
    i = [] 
    while k > 0:
        n = l[k - 1]
        k -= 1
        if n % 2 == 0:
            p.append(n)
        else:
            i.append(n)
    print('Lista Par:', p)
    print('Lista Ímpar: ', i)


l = []
k = 0 
s = 0
np = 0
spa = 0
while k < 10:
    n = int(input('n: '))
    l.append(n)
    k += 1
    s += n
    if n > 0:
        np += 1
    if n % 2 == 0:
        spa += 1

print('Lista: ', l)
print('Soma: ', s)
print('Média: ', s/k)
print('Quantidade de números Positivos: ', np)
print('Quantidade de pares:', spa)
lista(l,k)
invertida(l,k)
