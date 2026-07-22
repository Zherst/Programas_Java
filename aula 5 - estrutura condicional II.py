while True:
    try:
        n = float(input('dígite a nota: '))
        if 0 <= n <= 10:
            break
    except:
        print('dígite número entre 0 a 10')

if n >= 7:
    print('estudante aprovado')
elif 4 <= n < 7:
    print('estudante em recuperação')
else:
    print('estudante reprovado')