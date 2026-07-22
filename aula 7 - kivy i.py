from kivy.app import App
from kivy.uix.boxlayout import Boxlayout
from kivy.core.window import Window

class CampoAtuacaoEngenharia:
    def __init__(self):
        self.opcoes = ['','']
    def armazenaOpcoes(self,posicao,escolha):
        self.opcoes[posicao] = escolha

class Quadro(Boxlayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Window.size = (700,300)
    def selAtuacao(self,campo):
        minhaEscolha.armazenaOpcoes(1,campo)
    def geraResultado(self):
        curso = self.ids.txt1.text
        minhaEscolha.armazenaOpcoes(0,curso)
        final = f'Estou cursando atualmente {minhaEscolha.opcoes[0]} na PUCPR e seu principal \nramo é {minhaEscolha.campo[1]}'
        self.ids.resultado.text = final
    def Sair(self):
        App.get_running_app().stop()

class ExemploApp(App):
    def build(self):
        self.title = 'Exemplo usando Botões ...'
        return Quadro()

minhaEscolha = CampoAtuacaoEngenharia()
meuApp = ExemploApp()
meuApp.run()