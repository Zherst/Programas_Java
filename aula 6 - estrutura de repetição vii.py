while True:
    try:
        n = int(input('Dígite um número inteiro: '))
        
        if n > 0:
            print('O Valor é Positivo')
        else:
            print('O Valor é Negatico')
        r = input('Deseja repetir a execução? (s/n): ')
        while r != 's' and r != 'n':
            r = input('Deseja repetir a execução? (s/n): ')
        if r == 'n':
            print('encerrando... ')
            break
    except:
        print('Dígite um NÚMERO')