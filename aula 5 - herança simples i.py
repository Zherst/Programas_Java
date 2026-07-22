class conta:
    def __init__(self, **D):
        self.__numero = D.pop('numero', '--')
        self.saldo = D.pop('saldo', '--')
    def get_numero(self):
        return self.__numero
    def creditar(self, valor):
        self.saldo += valor
    def debitar(self, valor):
        self.saldo -=valor
class poupanca(conta):
    def __init__(self,**D):
        super().__init__(**D)
        self.rendimento = D.pop('rendimento', 0.0)
    def set_rendimento(self,taxa):
        self.rendimento += self.saldo  * taxa/100

c1 = conta(numero = '123-4', saldo = 1000)
c2 = poupanca(numero = '456-7', saldo = 2000)

c2.set_rendimento(10)
c2.set_rendimento(15)

print('número da conta 1:',c1.get_numero())
print('número da conta 2:',c2.get_numero())

print('saldo da conta 1:', c1.saldo)
print('saldo da conta 2:', c2.saldo + c2.rendimento)
