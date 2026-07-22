import math as mt

class cilindro:
    def __init__(self, r, h):
        self.raio = r
        self.altura = h
    
class matemática:
    __numero_pi = mt.pi
    __numero_euler = mt.e
    def __init__(self, n):
        self.numero = n

    def get_pi(self):
        return self.__numero_pi

    def get_e(self):
        return self.__numero_euler

    def seno(self):
        return mt.sin(self.numero)

    #objeto é um objeto cilindro
    def volume_cilindro(self, cilindro):
        area = self.__numero_pi * cilindro.raio ** 2
        volume = area * cilindro.altura
        return volume

mat = matemática(0)

print(mat.get_pi())
print(mat.get_e())

cil = cilindro(10, 20)
print('O volume é ', mat.volume_cilindro(cil))
    
    