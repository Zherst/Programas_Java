dia = int(input('forneça um número para o dia da semana'))

if dia <= 0 or dia > 7:
    print(' não existe dia da semana correspondente')
elif dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-Feira')
elif dia == 3:
    print('Terça-Feira')
elif dia == 4:
    print('Quarta-Feira')
elif dia == 5:
    print('Quinta-Feira')
elif dia == 6:
    print('Sexta--Feira')
else:
    print('Sábado')