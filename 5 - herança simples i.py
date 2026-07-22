from datetime import date

class pai:
    def __init__(self, **D):
        self.nome    = D['name']
        self.anoNasc = D['ano']
        self.sexo    = D.pop('sexo','__')
    def calcidade(self):
        agora = date.today()
        return agora.year - self.anoNasc
    
class filha(pai):
    def __init__(self, cor, compr, **dic):
        super().__init__(**dic)
        self.cabeloCor   = cor
        self.cabeloCompr = compr

fil1 = filha('castanho','longo',name='Angelica',ano=1999)
print(fil1.nome)
print(fil1.cabeloCor)
print(fil1.calcidade)

