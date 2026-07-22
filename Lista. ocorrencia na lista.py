def oc(n,l):
    k = 0
    cont = 0
    while k < len(l):
        if n == l[k]:
           cont += 1
        k +=1
    return cont

#------------------------------------

l = []
while True:
    v = int(input('Valor: '))
    if v == 0:
        break
    l.append(v)
n = int(input('Dígite um número: '))

print('esse número teve', oc(n,l) ,'ocorrências na lista')

