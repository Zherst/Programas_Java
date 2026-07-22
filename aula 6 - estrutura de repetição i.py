while True:
    x = float(input('Dígite um valor:'))
    if x == 0:
        break
    elif x > 0:
        print('O valor é positivo')
    else:
        print('O valor é negativo')
print('Deu zero.....encerrando')