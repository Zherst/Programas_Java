import math
m = math
def perim(r):
    return 2 * m.pi * r
def area(r):
    return m.pi * r ** 2
r = float(input('dígite o Raio: '))
print('perímetro: ', perim(r))
print('área: ', area(r))