class calculadora:
    def __init__ (self,opera1,opera2):
        self.operando1 = opera1
        self.operando2 = opera2
    def adicao(self):
        return self.operando1 + self.operando2
    def subtracao(self):
        return self.operando1 - self.operando2
    def multiplicacao(self):
        return self.operando1 * self.operando2
    def divisao(self):
        return self.operando1 / self.operando2
    def potenciacao(self):
        return self.operando1 ** self.operando2
    def raiz(self):
        return self.operando1 ** (1/self.operando2)



#================Programa principal====================
while True:
    try:
        op1 = float(input('dígite um número: '))
        op2 = float(input('dígite outro número: '))
        break
    except:
        print('válores tem que ser númericos!!')
opçao = input('Informe: + , - , x , / , pot , raiz: ')

while opçao not in '+-x/potraiz':
    print('opção inválida - verifique opções disponíveis')
    opçao = input('Informe: + , - , x , / , pot , raiz: ')

while op2 == 0 and opçao == '/':
    print('Divisao por zero não existe!!')
    while True:
        try:
            op2 = float(input('dígite outro número: '))
            break
        except:
            print('Operando inválido!!')
while (op2 <= 0 or op1 < 0) and opçao == 'raiz':
    print('Radicando e radical tem que ser positivo!!')
    while True:
        try:
            op1 = float(input('dígite outro número op1: '))
            op2 = float(input('dígite outro número op2: '))
            break
        except:
            print('Radicando e radical tem que ser um número')
#========criação do objeto claculadora==========
c = calculadora(op1,op2)
if opçao == '+':
    print('A soma vale: ',c.adicao())
elif opçao == '-':
    print('A subtração vale: ',c.subtracao())
elif opçao == 'x':
    print('A multiplicação vale: ',c.multiplicacao())
elif opçao == '/':
    print('A divisão vale: ',c.divisao())
elif opçao == 'pot':
    print('A potenciação vale: ',c.potenciacao())
else:
    print('A raiz vale: ',c.raiz())

