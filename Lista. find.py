def achei(x, lista):
    k = 0
    while k < len(lista):
        if x == lista[k]:
            return True
        k = k + 1
    return False

# PROGRAMA PRINCIPAL
l =[]
while True:
    v = int(input('Valor: '))
    if v == 0:
        break
    l.append(v)
    
print(l)
n = int(input('dígite o valir a ser procurado: '))
if achei(n,l) == True:
    print('O número ', n, 'consta na lista.')
else:
    print('O número', n , 'não consta na lista.')