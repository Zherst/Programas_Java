n = float(input('Dígite um númerador: '))
d = float(input('Dígite um denominador: '))

while d == 0:
    d = float(input('Erro....dígite um novo denominador: '))

res = n/d
print('Resposta: ', res)    