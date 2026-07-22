c = 0
p = 0
i = 0
ci = 0
while True:
    n = int(input('Dígite um número inteiro: '))
    if n == 0:
        break
    elif n % 2 == 0:
        p = p + n
    else:
        i = i + n
        ci = ci + 1
    c = c + 1
print('Total de valores: ', c)
print('Soma dos valores Pares: ', p)
if ci != 0:
    i = i/ci
    print('média dos valores ímpares: ', i)
else:
    print('não tem média do ìmpar')