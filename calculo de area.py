base= float(input('Base:'))
while base <= 0:
    print('Erro!!!');
    base= float(input('Base:'))
altura = float(input('Altura:'))
while altura <= 0:
    print('Erro!!!');
    altura = float(input('Altura:'))
area = (base*altura) / 2
print(f'A área de um retângulo com base {base} e altura {altura} vale {area}')