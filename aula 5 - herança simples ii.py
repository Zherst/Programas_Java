class artista:
    def __init__(self,nome,**D):
        self.nome = nome 
        self.nacionalidade = D.pop('nacionalidade', '--')

class filme:
    def __init__(self,titulo,**D):
        self.__titulo = titulo
        self.ano = D.pop('ano', '--')
        self.descricao = D.pop('descricao', '--')
        self.genero = D.pop('genero', '--')
    def get_titulo(self):
        return self.__titulo

class ator(artista):
    def __init__(self,nome,**D):
        super().__init__(nome,**D)
        self.data_inicio = D.pop('data_i', '--')
        self.filme = []
        if 'filme' in D:
            for f in D['filme']:
                self.filme.append(f)
    def add_filme(self,filme):
        self.filme.append(filme)

    
f1 = filme('a era do gelo', )
f2 = filme('a')

a1 = ator('carlos', filme = f1, filme = f2)

