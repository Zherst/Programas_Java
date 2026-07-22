vi = float(input('defina um Valor inicial:'))
vf = float(input('defina um Valor final:'))

while vi >= vf:
    print('valor inicial Tem que ser menor que o final.')
    vi = float(input('defina um Valor inicial:'))
    vf = float(input('defina um Valor final:'))

r = float(input('defina uma Razão:'))
while r <= 0:
    print('razaão não pode se menor ou igual a 0')
    r = float(input('defina uma Razão:'))
    
while vi <= vf :
    print(vi)
    vi = vi + r