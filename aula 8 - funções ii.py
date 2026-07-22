def fat(n):
    i = 1
    r = 1
    while i <= n:
        print(f'N: {i-1} | N!: {r} ')
        r = r * i
        i += 1
    print(f'N: {i-1} | N!: {r} ')
    return 
n = int(input('Dígite um númuro inteiro: '))
fat(n)