from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class Tela(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Windou.size = (400,400)
        self.preco = {'Cimento Portland (50)': 50,
                        'Concreto Usinado (30)': 30,
                        'Manta Alifatica (10m)': 10}
        self.soma = 0
    
    def selecao(self,situacao,produto,qtde):
        if situacao:
            try:
                quantidade = int[qtde]
                self.soma += int[qtde]*self.preco['Cimento Portland (50)','Concreto Usinado (30)', 'Manta Alifatica (10m)']
                self.ids.mensagemErro.text = ' '
            except:
                self.ids.mensagemErro.text = '[b]Qantidadeinvalida!![/b]'
                if produto == 'Cimento Portland (50)':
                    self.ids.ck1.active = False
                elif produto == 'Concreto Usinado (30)':
                    self.ids.ck2.active = False
                else:
                    self.ids.ck3.active = False

    def pagamento(self,tipo):
        if tipo == 'A vista (-5%)':
            self.soma -= (self.soma*5/100)
        elif tipo == '2 vezes (+2,5$)':
            self.soma += (self.soma*2.5/100)
        else:
            self.soma += (self.soma*8/100)
        self.ids.resultado.text = f'A pagar R$ {round(self.soma,2)}'

    def limpa(self):
        self.ids.ck1.active = False
        self.ids.ck2.active = False
        self.ids.ck3.active = False
        self.ids.prod1.text = ' '
        self.ids.prod2.text = ' '
        self.ids.prod3.text = ' '
        self.ids.mensagemERRO.text = ' '
        self.ids.resultado.text = 'A pagar R$'
        self.soma = 0

class provaApp(App):
    def build(self):
        return Tela()

provaApp().run
