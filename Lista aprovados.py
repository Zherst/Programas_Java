
nomes=[]
p1=[]
p2=[]
f=[]
s = 0
k = 0
while True:
    while True:
        try:
            a = input('Dígite um nome: ')
            if a == '':
                break
            b = float(input('nota 1: '))
            while b < 0 or b > 10:
                print('Nota é válida entre 0 e 10')
                b = float(input('nota 1: '))
            c = float(input('nota 2: '))
            while c < 0 or c > 10:
                print('Nota é válida entre 0 e 10')
                c = float(input('nota 2: '))
            d = float(input('% de frequencia: '))
            while d < 0 or d > 100:
                print('% de frequencia é valido entre 0% e 100%')
                d = float(input('% de frequencia: '))
            
            break
        except:
            print(' Atenção aos TIPOS de dados fornecidos!!!')
    if a == '':
        break
    nomes.append(a)
    p1.append(b)
    p2.append(c)
    f.append(d)
nome = input('Dígite o nome do aluno: ')
for x in nomes:
    if x == nome:
        n = nomes.index(nome)
if  n == 999:
    print('nome não encontrado')
print('Aluno(a) ', nomes[n],'com Média ', media,'com frequencia', f[n], )