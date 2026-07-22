
class contab:
    def __init__(self, a, c, s):
        self.agencia = a
        self.conta = c
        self.__saldo = s
    def m_saldo(self):
        return self.__saldo
        
    
class cliente:
    def __init__(self, n, cpf):
        self.nome = n
        self.__cpf = cpf

    def m_cpf(self):
        return self.__cpf
    
    def m_conta(self, nova_c):
        return f'CC de {self.nome}: ag.: {nova_c.agencia}, nº: {nova_c.conta} e saldo: R${nova_c.m_saldo()}'

#________PROGRAMA PRINCIPAL____________

no = input('Nome do Correntista: ')
while no =='':
    print('nome inválido')
    no = input('Nome do Correntista: ')

CPF = input('CPF:')
while CPF =='':
    print('CPF inválido')
    CPF = input('CPF:')    

ag = input('Agencia nº: ')
while ag =='':
    print('Agencia inválido')
    ag = input('Agencia nº: ')

CC = input('Conta nº: ')
while CC =='':
    print('Conta nº inválido')
    CC = input('Conta nº: ')
while True:
    try:
        sd = float(input('Saldo: R$'))
        while sd <= 0:
            print('saldo tem que ser maior que zero')
            sd = float(input('Saldo: R$'))
        break
    except:
        print('Saldo tem que ser número')
#________________CRIAÇÃO DOS OBJETOS
            
cc1 = contab(ag,CC,sd)
cli1 = cliente(no,CPF)
print(f'Agencia: {cc1.agencia}')
print(f'CC: {cc1.conta}')
print(f'Saldo: R$ {cc1.m_saldo()}')
print(f'Nova conta: {cli1.m_conta(cc1)}')