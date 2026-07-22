def letras(*lista):
    print(lista)
    texto = ''
    for i in lista:
        texto = texto + 1
    return texto
def somatoria(*numeros):
    s = 0
    for n in numeros:
        s += n
    return s 
    
print(letras("a", "b", "c"))
