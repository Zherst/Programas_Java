num1 = float(input('ínsira a:'))
num2 = float(input('ínsira b:'))
num3 = float(input('ínsira c:'))

if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print (' Não Existem lados Negativos ou Nulos!!!')
else:
    if num1 > num2 + num3 or num2 > num1 + num3 or num3> num1 + num2:
        print('Não Forma Triangulo;')
    elif num1 == num2 == num3:
        print('Triagulo Equilátero')

    elif num1 == num2 or num2 == num3 or num1 == num3:
        print(' Triangulo Isósceles')

    else:
        print(' Triangulo Escaleno')