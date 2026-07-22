class cliente:
    def __init__(self, nome, CPF, contasb):
        self.n = nome
        self.__cpf = CPF
        self.listab = []
        for x in contasb:
            self.listab.append(x)
    def get_cpf(self):
        return self.__cpf

class contab:
    def __init__(self, agencia, conta, saldo):
        self.ag = agencia
        self.con = conta
        self.__sal = saldo
    def get_sal(self):
        return self.__sal
    def faz_saque(self, saldo):
        self.__sal -= saldo
    def faz_deposito(self, saldo):
        self.__sal += saldo

class livro:
    def __init__(self, titulo, autor, preco, total):
        self.titu = titulo
        self.aut = autor
        self.preco = preco
        self.exemplares = total
    def estoque(self):
        return self.exemplares > 0
    def venda(self):
        if self.estoque():
            self.exemplares -= 1
            return('livro vendido')
        else:
            return('livro indisponivel')
#=====================menu===================
def imprimeTela():
    print('\n================opções do programa================')
    print('< 1 > Fazer Saque')
    print('< 2 > Fazer Deposito')
    print('< 3 > Consulta Simples')
    print('< 4 > ')
listacc = []
while True:
    ag = input('Agência: ')
    while ag == '':
        ag = input('Agência: ')
    con = input('Conta Nº: ')
    while con == '':
        con = input('Conta Nº: ')
    while True:
        try:
            saldo = float(input('Saldo da Conta: '))
            while saldo <= 0:
                print('não é aceito valor negativo')
                saldo = float(input('Saldo da Conta: '))
            break
        except:
            print('saldo tem que ser um número')

    listacc.append( contab (ag, con, saldo))
    op = input('continua (s/n)').upper()
    while op not in['s','n']:
        print('responda s ou n')
        op = input('continua (s/n)').upper()
    if op == 'n':
        break                  

nome = input('nome: ')
while nome == '':
    nome = input('nome: ')
cpf = input('C.P.F: ')
while cpf == '':
    cpf = input('C.P.F: ')

cliente1 = cliente(nome, cpf, listacc)

while True:
    imprimeTela()
    while True:
        try:
            opcao = int(input('Dígite a opção disponível'))
            while opcao < 0 or opcao > 3:
                print('Opção inválida')
                opcao = int(input('Dígite a opção disponível'))
            break
        except:
            print('tem que ser um número')
        if opcao == 0:
            print('encerrando programa....')
        elif opcao == 1 or opcao == 2:
            saldo = float(input('Valor pra saque/deposito: '))
            for x in cliente1.listab:
                print(f'Agencia: {x.ag} - conta Nº: {x.con} - Saldo: R${x.get_sal()}')
            pos = int(input('posição da conta:'))
            if opcao == 1:
                cliente1.listab[pos].faz_saque(saldo)
            else:
                cliente1.listab[pos].faz_deposito(saldo)
            print(f'Agência: {cliente1.listab[pos].ag} - Conta Nº: {cliente1.listab[pos].con} - Saldo: R${cliente1.listab[pos].get_sal()}')
            input('ENTER para continuar ....')
        else:
            print(f'Cliente: {cliente1.nome} = C.P.F.: {cliente1.get_cpf()} possui as contas: ')
            for x in cliente1.listab:
                print(f'Agência: {x.agencia} = Conte Nº: {x.conta} = saldo: R${x.get_sal()}')

            total = 0
            for x in cliente1.listab:
                total += x.get_sal()
            print(f'Totalizando um montante de R${total}')
            input('tecle ENTER para continuar ....')