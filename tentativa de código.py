
cont=0
soma=0
valor=int(input('Dígite um valor:'))
menor= valor
maior = valor
while True:

    soma = soma + valor
    cont = cont + 1
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    resp = input('continua (S/N)?: ')

    if resp =='S' or resp == 's':
        valor=int(input('Dígite um valor:'))
    
    if resp == "N" or resp == "n":
                break
    else:
        print('resposta invalida!!!!')
 
    
print('encerrando...')
print('Soma:', soma)
print('Média:', round(soma/cont,4))
print('Maior valor:', maior)
print('menor valor:', menor)