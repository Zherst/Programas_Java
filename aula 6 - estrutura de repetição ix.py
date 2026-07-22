def menu():
    print('===========MENU===========')
    print('<1> Adição')
    print('<2> Subtração')
    print('<3> Multiplicação')
    print('<4> Divisão')
    print('<0> Sair')
    print('==========================')

def adicao(n):
    s = 1
    while s < 11:
        print(f'{n} + {s} = {n+s}')
        s +=1

def subtracao(n):
    s = 1
    while s < 11:
        print(f'{n} - {s} = {n-s}')
        s +=1

def multiplicacao(n):
    s = 1
    while s < 11:
        print(f'{n} x {s} = {n*s}')
        s +=1

def divisao(n):
    s =1
    while s < 11:
        print(f'{n} / {s} = {n/s}')
        s +=1

while True:
    try:
        menu()
        op = 0
        op = int(input('Opção: '))
        if op == 0:
            print('encerrando...')
            break
        while  op < 0 or op > 4:
            print('Dígite um número do menu')
            op = int(input('Opção: '))
        n = int(input('Dígite um número de 1 a 10 para a tabuada: '))
        while n < 1 or n > 10:
            print('Dígite entre 1 e 10')
            n = int(input('Dígite um número de 1 a 10 para a tabuada: '))
    except:
        print('Dígite um número')
    if op == 1:
        adicao(n)
    if op == 2:
        subtracao(n)
    if op == 3:
        multiplicacao(n)
    if op == 4:
        divisao(n)
    