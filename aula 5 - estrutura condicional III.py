while True:
    try:
        h = float(input('dígite a sua altura:'))
        while h <= 0:
            print('dígite um valor positivo maior que zero')
            h = float(input('dígite a sua altura:'))
        n = input('sexo masculino ou feminino?(m/f): ')
        if n == 'm':
            p = (72.7*h)-58
            print(p)
        elif n =='f':
            p = (62.1*h)-44.7
            print(p)
        elif n == 'no':
            break
        else:
            print('dígite m pra masculino ou f pra feminino')
    except:
        print('dígite um número')        