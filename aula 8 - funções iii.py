def soma(a,b):
    r = a + b
    return r
def subitração(a,b):
    r = a - b
    return r
def multiplicação(a,b):
    r = a * b
    return r
def divisão(a,b):
    r = a / b
    return r
print('|Operação Matemáticas: |')
print('|Soma               (1)|')
print('|Subtração          (2)|')
print('|Multiplicação      (3)|')
print('|Divisão            (4)|')
while True:
        o = int(input('dígite o número da opção: '))
        while o > 4 or o < 1:
                    o = int(input('dígite o número dentre das opção: '))
        print('informe os valores de ')
        a = int(input('a = ' ))
        b = int(input('b = '))
        if o == 1:
            print(f'{a} + {b} = {soma(a,b)}')
        elif o == 2:
            print(f'{a} - {b} = {subitração(a,b)}')
        elif o == 3:
            print(f'{a} * {b} = {multiplicação(a,b)}')
        else:
            print(f'{a} % {b} = {divisão(a,b)}')
        r = int(input('dígite 0 se quiser continuar a operação: '))
        if r == 0:
             break

        
