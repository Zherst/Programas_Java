class endereco:
    def __init__(self, r, n, c, e, cep):
        self.rua = r
        self.numero = n
        self.ciade = c
        self.estado = e
        self.__CEP = cep
    
    def get_CEP(self):
        return self.__CEP
        pass






class pessoa:
    def __init__(self, n, e, i, cpf, nick):
        self.__nome = n
        self.__endereco = e
        self.__idade = i
        self.__CPF = cpf
        self.apelido = nick
    
    def get_nome(self):
        return self.__nome
    
    def get_endereco(self):
        return self.__endereco

    def get_CPF(self):
        return self.__CPF
    
    def get_idade(self):
        return self.__idade
    
end = endereco('Rua Zero', 100,"Curitiba", 'Paraná' ,'80800800')
p1 = pessoa('Josefino', end, 25, "123456789-12", "Canela")

print('A rua = ', p1.get_endereco().rua)

p1.get_endereco().rua = "Rua esquina"
print('A rua = ', p1.get_endereco().rua)

