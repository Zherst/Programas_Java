# orfenação usando métido bolha ou Bubble Sort
def ordenaC(lista):
    for vezes in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:#sinal de > ordena crescente
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista
def ordenaD(lista):
    for vezes in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] < lista[i + 1]:#sinal de < ordena decrescente
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista

#==========================Programa Principal================================
numeros = [10,-8,44,0,-11,5]
print('Números em ordem crescente: ', ordenaC(numeros))
preços = [8.88,8.9,-10.4,-10.5,8,0]
print('Preços em ordem decrescente: ', ordenaD(preços))
letras = ['Z','J','A','W','B']
print('Letras em ordem crescente: ', ordenaC(letras))
nomes = ['Marios','Mari','Maria','Mariazinha','Mariana']
print('Nomes em ordem crescente', ordenaC(nomes))
input()
            