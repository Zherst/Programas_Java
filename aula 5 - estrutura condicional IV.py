while True:
    n = int(input('número(dígite 0 pra ternminar):'))
    if n == 0:
        break
    elif n % 2 == 0:
        p = n
        print('par: ', p)
    else:
        i = n
        print('ímpar: ', i)
