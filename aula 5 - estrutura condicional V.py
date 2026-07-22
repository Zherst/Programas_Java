while True:
    try:
        i = float(input('informw a sua idade: '))
        if i <= 15:
            print('você não pode subir na montanha russa, é menor que 15 anos')
            break
        p = float(input('informe o seu peso: '))
        if p > 120:
            print('você não pode subir na montanha russa, pesa mais que 120 kg')
            break
        else:
            print('está autorizado a ir')
            break
    except:
        print('dígite um número')
