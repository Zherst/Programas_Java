nomes = []
while True:
    nome = input('Dígite o nome desejado: ')
    if nome == '':
        print('Lista informada com sucesso!!!')
        break
    nomes.append(nome)
original = nomes.copy()
print('Lista original: ', nomes)
nomes.sort()
print('Lista em ordem alfabética crescente: ',nomes)
nomes.sort(reverse=True)
print('Lista em ordem decrescente: ', nomes)
