L=[]
P=[]
I=[]
k = 0
n = int(input('Dígite um inteiro positivo: '))
while k < n:
    x = int(input('dígite um número:'))
    L.append(x)
    if x % 2 ==0:
        P.append(x)
    else:
        I.append(x)
    k +=1
print('lista: ', L)
print('pares da lista: ', P)
print('impares da lista: ', I)

      

