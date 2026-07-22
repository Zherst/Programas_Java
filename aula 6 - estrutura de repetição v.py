while True:
    A = float(input('Dígite o preço (R$) no mercado A:'))
    B = float(input('Dígite o preço (R$) no mercado B:'))
    if A > B:
        print('O Mercado B tem o menor preço')
    else:
        print('O Mercado A tem o menor preço')
    r = str(input('Deseja repetir a execução? (s/n): '))
    while r != 's' and r != 'n':
        r = input('Deseja repetir a execução? (s/n): ')
    if r == 'n':
        break
        
