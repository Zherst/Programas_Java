n = int(input('n: '))
while n <= 0:
    print('Erro')
    n = int(input('n: '))  
S = 0
cont = 1
den = 1
while cont <= n:
    termo = 1/den
    S = S + termo
    den = den * 2
    cont = cont + 1
print('S= ', S)
    