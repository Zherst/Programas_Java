def somatorio1(n):
    s = 0
    k = 1
    while k <= n:
        s += k ** 2
        k += 1
    return s
def fatorial(termo):
    fat = 1
    while termo > 0:
        fat *= termo
        termo -= 1
    return fat
def somatorio2(n):
    s = 0
    k = 1
    while k <= n:
        s += 1/ fatorial(2*k-1)
        k += 1
    return s
def somatorio3(n):
    s = 0
    k = 1
    while k <= n:
        s += k/3**k
        k += 1
    return s

while True:
    print('\n'*50)
    print('***********************************************');
    print('* <1> Somatório 1 + 4 + 9 + 16 + ............ *');
    print('* <2> Somatório 1 + 1/3 + 1/5 + 1/7 + ....... *');
    print('* <3> Somatório 1/3 + 1/9 + 1/27 + 1/81 + ... *');
    print('* <0> Encerrar o programa ................... *');
    print('***********************************************');
    op = int(input('digite o número da opção desejada: '));
    
    while op < 0 or op > 3:
        print('opção inválida! dígite número de 0 a 3')
        op = int(input('digite o número da opção desejada: '))
        
    if op == 0:
        print('Encerrando o programa...')
        break
    else:
        n = int(input('Quantos termos para o somatório? '))
        while n <= 0:
            print('quantidade deve ser positiva');
            n = int(input('Quantos termos para o somatório? '))
            
            
        if op == 1:
            soma = somatorio1(n)
            print('resultado do soma vale ',soma)
            
        elif op == 2:
            soma = somatorio2(n)
            print('resultado do soma vale ',round(soma,4))
            
        else:
            soma = somatorio3(n)
            print('resultado do soma vale ',round(soma,1));
    input('tecle < ENTER > para continuar.....')