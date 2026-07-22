I = int(input('Idade: '))
if I <= 0:
    print ('Idade Inválida!!!!')
elif I < 16:
    print(' Não Eleitor')
elif 18 <= I <= 65:
    print('Eleitor Obrigatório')
else:
    print('Eleitor Facultativo')