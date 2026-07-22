n = int(input('n: '))
while n <= 0:
    print ("ERRO!!!!");
    n = int(input('n: '))
cont = 0
i = 1
while i <= n:
    if n % i == 0:
        cont = cont + 1
        print(i)
    i = i + 1
if cont == 2:
    print(n,'é primo')
else:
    print(n,'não é primo')