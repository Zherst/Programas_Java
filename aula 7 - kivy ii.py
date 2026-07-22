from kivy.app import App
from kivy.widget import widget

class Tela(widget):
    pass
class AulaApp(App):
    def build(self):
        self.title = "Meu primeiro App"
        return(Tela)
    
AulaApp().run()

