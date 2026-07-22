nota = float(input('Digite sua nota'))
if nota < 0 or nota >10:
    print('Nota Inválida!!!')
else:
    if nota < 4:
        print('reprovado por',nota)
    else:
        if nota >= 7:
            print('aprovado',nota)
        else:
            print('Em exame por',nota)
            