class cidade:
    def __init__ (self, nome, data_fundacao, populacao):
        self.__n = nome
        self.dt = data_fundacao
        self.p = populacao
    def get_nome(self):
        return self.__n

class estado:
    def __init__(self, nome, reg, capital):
        self.__n = nome
        self.re = reg
        self.cap = capital

    def get_nome(self):
        return self.__n
    
    def set_nome(self, nome):
        self.__nome = nome 

class pais:
    def __init__(self, nome, populacao, moeda, lingua, *estados):
        self.__n = nome
        self.pop = populacao
        self.moe = moeda
        self.lin = lingua
        self.__estado = []
        for i in estados:
            self.__estado.append(e)
    def get_nome(self):
        return self.__n
    
    def get_estado(self):
        return self.__estado
    
    def ass_estado(self, estado):
        self.__estado.append(estado)
    
        

c1 = cidade('curitiba','29/03/1793','150000')
c2 = cidade('biturub', '30/06/1910', '5800')
c3 = cidade('Florianópolis', '09/12/1850', '11254')
c4 = cidade('belo horizonte', '24/05/1930', '211552')

e1 = estado('Paraná', 'Sul', c1)
e2 = estado('São Paulo', 'Sudeste', cidade('São paulo', 'bem veia', "200000000"))
e3 = estado('Santa catarina', 'sul', c3)
e4 = estado('Minas gerais', 'suldeste', c4)

p1 = pais('Brasil', 54000000, 'Real', 'Português', e1, e2, e3, e4)

print('País: ', p1.get_n())
print('População: ', p1.pop())
print('Estado: ')
print('nome     -      capital')
for e in p1.get_estado():
    print(e1.get_n(), '-', e1.capital.get_nome())
    

