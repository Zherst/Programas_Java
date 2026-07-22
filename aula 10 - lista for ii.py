t = int(input('tamanho da lista: '))
l =[]
maior = 0
menor = 0
for i in range(t):
    n  = int(input('n:'))
    l.append(n)
    if i == 0:
        maior = n
        menor = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
print(l)
print('maior: ', maior)
print('menor: ', menor)