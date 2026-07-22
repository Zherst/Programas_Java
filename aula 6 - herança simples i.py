from datetime import date
class endereco:
    def __init__(self,**d):
        self.rua = d.pop('rua', '--')
        self.num = d.pop('num', '--')
        self.bairro = d.pop('bai', '--')
        self.cidade = d.pop('cid', '--')
        self.estado = d.pop('est', '--')

class pessoa(endereco):
    def __init__(self,**d):
        super().__init__ (self,**d)
        self.anon = d.pop('ano', 2000)
        self.sexo = d.pop('sexo', '--')
        self.altura = d.pop('alt', 1.7)
        self.peso = d.pop('peso', 6.5)
    def calc_idade (self):
        x = date.today()
        return x.year - self.anon 
    def calc_imc (self):
        return self.peso/self.altura ** 2
    def por_extenso(self):
        abreviado = self.sexo.upper()
        return

class artista(pessoa):
    def __init__(self,**d):
        super().__init__(self,**d)
        self.nome = d.pop('nom', 'Rui')
        self.nacionalidade = d.pop('nac', 'Brazuca')

class filme:
    def __init__(self,**d):
        self.titulo = d.pop('tit', '--')
        self.ano = d.pop('ano', 2000)
        self.descricao = d.pop('desc', '--')
        self.genero = d.pop('gen', '--')

class ator(artista):
    def __init__(self,**d):
        super().__init__(self,**d)
        self.data_filme = d.pop('dat', '--')
        self.filme = []
        for x in listaf:
            self.filme.append(x)
    def add_filme (self, filme):
        return self.filme.append(filme)
