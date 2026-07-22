def primo(n):
    cont = 0
    i = 1
    while i <= n:
        if n % i == 0:
            cont = cont + 1
        i = i + 1
    if cont == 2:
        return True
    else:
        return False
def SOMA1(q):
    soma = 0
    k = 1
    while k <= q:
        soma = soma + k * (-1) ** (k+1)
        k = k + 1
    return soma
def SOMA2(q):
    ant = 1
    prox = 0
    k = 1
    soma = 0
    while k <= q:
        atual = ant + prox
        ant = prox
        prox = atual
        soma = soma + atual
        k = k + 1
    return soma
def SOMA3(q):
    k = 1
    s = 0
    n = 1
    a = False
    while k <= q:
        while a == False:
            n += 1
            a = primo(n)
        s += n
        k += 1
        a = False
    return s

def SOMA4(q):
    fat = 1
    k = 1
    a = 1
    s = 0
    while k <= q:
        b = a
        while a > 0:
            fat *= a
            a -= 1
        a = b + 2
        s += fat
        fat = 1
        k = k + 1
    return s
    

# ======================== Script Principal

while True:
    print('******************* Escolha a opção desejada *******************');
    print('* <1> SI = 1 - 2 + 3 - 4 + 5 + ................................*');
    print('* <2> SII = 1 + 1 + 2 + 3 + 5 + 8 + 13 + ......................*');
    print('* <3> SIII = 2 + 3 + 5 + 7 + 11 + 13 + ........................*');
    print('* <4> SIV = 1! + 3! + 5! + 7! + 9! + ..........................*');
    print('* <0> Sair do Programa.........................................*');
    print('****************************************************************');
    
    op = int(input('Dígite o número do somatório desejado: '));
    while op <0 or op >4:
        print('opção não dísponivel, escolha entre 0 a 4')
        op = int(input('Dígite o número do somatório desejado: '))
    if op == 0:
        print('Encerrando programa...')
        break
    else:
        n = int(input('Quantos termos para o somátorio?'))
        while n<= 0:
            n = int('Quantos termos para o somátorio?')
        if op == 1:
            s = SOMA1(n)
            print('O somatório I vale',s);
        elif op == 2:
            s = SOMA2(n)
            print('O somatório II vale',s);
        elif op == 3:
            s = SOMA3(n)
            print('O somatório III vale',s);
        else:
            s = SOMA4(n)
            print('O somatório IV vale',s);
        input('Tecle <ENTER> para continuar....');