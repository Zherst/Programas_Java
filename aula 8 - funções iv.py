def primo(n):
    i = 1
    cont = 0
    while i <= n:
        if n % i == 0:
            cont += 1
        i += 1
    if n == 1:
        return n
    elif cont == 2:
        return n
    else:
        return False

def n_primo(n):
    i = 1
    while i <= n:
        if primo(i) != False:
            print(i)
        i += 1 

def soma(n):
    i = 1
    soma = 0
    while i <= n:
        if primo(i) != False:
            soma += i
        i += 1
    print(soma)
#==================================================================
n = int(input('n: '))
while n <= 0:
    print ("ERRO!!!!")
    n = int(input('n: '))
if primo(n) != False:
    print(f'{n} é primo')
else:
    print(f'{n} ñ é primo')
print(f'Primos até {n}: ')
n_primo(n)
print('Soma dos Primos: ')
soma(n)
