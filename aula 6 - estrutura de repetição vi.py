c = 0
s = 0
while True:
    n = int(input('dígite um valor:'))
    c += 1
    s  = s + n
    if n == 0:
        c -= 1
        print("encerrando...")
        break
print('Soma dos valores: ', c )
print('média entre os números: ', s/c)
