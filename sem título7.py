import matplotlib.pyplot as plt
import math as mt

fig = plt.figure(figsize=(10, 8))

xm = 0.08
t = 1.710
phi = 0
om = (2*mt.pi/t)

velocidade = [] #Eixo Y
tempo = [] #Eixo X

abscissa = [0,t/4,t/2,3*t/4,t] #x1,x2,x3...
ordenada = [0,-0.310,0,0.310,0] #y1,y2,y3...

plt.plot(abscissa , ordenada , 'ro')
plt.xlabel("Tempo(s)" , fontsize = 'x-large')
plt.ylabel("Velocidade(m/s)" , fontsize = 'x-large')
plt.title("Renato Guan")

for x in range(0,250):
  x=x /100
  y=-xm*om*mt.sin(om*x+phi)
  velocidade.append(y)
  tempo.append(x)

plt.plot(tempo , velocidade , lw = 3)

plt.savefig("grafico_velocidade.png")