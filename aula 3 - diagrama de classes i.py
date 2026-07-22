class pessoa:
    def __init__(self, np, ip, pp, ap):
        self.__nome = np
        self.__idade = ip
        self.__peso = pp
        self.__altura = ap
        
    def envelhecer(self, anos):
        self.idade += anos

    def engordadar(self, kgs):
        self.peso += kgs
    
    def emagrecer(self, kgs):
        self.peso -= kgs

    def crescer(self, medida):
        self.altura += medida

    def mostrar_nome(self):
        return self.__nome

pessoa1 = pessoa('Josefino', 10, 25, 1.2)

print(pessoa1.idade)
print(pessoa1.peso)
print(pessoa1.mostrar_nome())
pessoa1.envelhecer(5)
print('nova idade = ', pessoa.idade)

