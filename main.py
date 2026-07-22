from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader

class planetario(BoxLayout):
    imagem_fundo = StringProperty("terra.jpg")

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.som_terra = SoundLoader.load("somTerra.wav")
        self.som_lua = SoundLoader.load("somLua.wav")
        self.som_saturno = SoundLoader.load("somSaturno.wav")
        self.som_jupiter = SoundLoader.load("somJupiter.wav")
    def muda_gravidade(self,planeta):
        if planeta == "terra":
            self.ids.mensagem.text = "planeta terra"
            self.imagem_fundo = "terra.jpg"
            self.som_terra.play()
        elif planeta == "lua":
            self.ids.mensagem.text = "planeta lua"
            self.imagem_fundo = "Lua.jpg"
            self.som_lua()
        elif planeta == "saturno":
            self.ids.mensagem.text = "planeta saturno"
            self.imagem_fundo = "saturno.jpg"
            self.som_saturno.play()
        elif planeta == "jupiter":
            self.ids.mensagem.text = "planeta jupiter"
            self.imagem_fundo = "jupiter.jpg"
            self.som_jupiter.play()
        elif planeta == "urano":
            self.ids.mensagem.text = "planeta urano"
            self.imagem_fundo = "urano.jpg"
        elif planeta == "netuno":
            self.ids.mensagem.text = "planeta netuno"
            self.imagem_fundo = "netuno.jpg"
    def define_som(self,marcado):
        volume = 0
        if marcado == True:
            volume = 1
        self.som_jupiter.volume = volume
        self.som_lua.volume = volume
        self.som_saturno.volume = volume
        self.som_terra.volume = volume
    def sair(self):
        App.get_running_app().stop()
class planetario(App):
    def build(self):
        Window.size = (400,600)
        self.title = "planetario"
        return Tela()
    
planetario().run()