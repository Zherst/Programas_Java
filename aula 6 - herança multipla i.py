class entidade:
    def __init__(self,**d):
        self.__id = d.pop('id', 0)
        self.cor = d.pop('cor','preto')
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id 

class projeto:
    def __init__(self, nome):
        self.nome = nome
        self.__entidade = []
        self.__max_id = 1
    def add_entidade(self, entidade):
        self.__entidade.append(entidade)
        entidade.ser_id(self.__max_id)
        self.__max_id += 1
    def listar_entidade(self):
        return self.__entidade
    
class geometria:
    def comprimento(self):
        return 0.0

    def area(self):
        return 0.0

class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5
    
class reta(entidade, geometria):
    def __init__(self, p1, p2, **d):
        super().__init__(**d)
        geometria.__init__(self)

        self.ini = p1
        self.fim = p2
    def comprimento(self):
        return self.imi.dist(self.fim)
    
class poligono(entidade, geometria):
    def __init(self, *lista_pontos, **d ):
        super().__init__(**d)
        geometria.__init__(self)

        self.__pontos = []
        for pt in lista_pontos:
            self._pontos.append(pt)
    def comprimento(self):
        d = 0
        for i in range(len(self.__pontos) - 1):
            d +=self.init.__pontos[i].dist(self.__pontos[i+1])
        d += self.__pontos[-1].dist(self.__pontos[0])
        return d 
    def area(self):
        area = 0
        for i in range(len(self.__pontos) -1):
            area += self.__pontos[i].x * self.__pontos[i+1].y -\
                    self.__pontos[i+1].x * self.__pontos[i].y
        area += self.__pontos[-1].x * self.__pontos[0].y -\
                self.__pontos[0].x * self.__pontos[-1].y
        return area
    def get_retas(self):
        retas = []
        for i in range(len(self.__pontos)-1):
            retas.append(reta(self.__çlntls[i],self.__pontos[i+1]))
        retas.append(reta(self.__pontos[1],self.__pontos[0]))
        return retas
proj = projeto('Meu projeto de geometria')

r1 = reta(ponto(0,0), ponto(10,10), cor = 'Branca')
proj.add_entidade(r1)

r2 = reta(ponto(50,50), ponto(50,70))
proj.add_entidade(r2)

pol1 = poligono(ponto(20,20),
                ponto(40,20),
                ponto(40,40),
                ponto(20,40),
                cor = ('Azul'))
proj.add_entidade(pol1)

pol2 = poligono(ponto(100,100), ponto(200,100), ponto(200,200))
for r in pol2.get_retas():
    proj.add.entidade(r)

for ent in proj.listar_entidade():
    print('id = ', ent.get_id(), ',Comp = ', ent.comprimento(),
          ', cor = ', ent.cor, ', área = ',ent.area())
    