a = int(input('a: '))
if a != 0:
    print('Não é equação de 2º grau')
else:
    b = int(input('b: '))
    c = int(input('c: '))

    d = b ** 2 - 4 * a * c
    if d < 0:
        print('não há raizes reais')
    elif d > 0:
        r1 = (-b + d ** 0.5)/(2 * a)
        r2 = (-b - d ** 0.5)/(2 * a)
        print('Duas raizes: ', r1, r2)
    else:
        r = -b / (2 * a)
        print('Uma raiz: ', r)



