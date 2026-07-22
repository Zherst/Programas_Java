import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))

abscissa = [0.086,0.127,0.196,0.273,0.415] #x1,x2,x3...
ordenada = [0.488,0.976,1.464,1.952,2.44] #y1,y2,y3...

a = 6.772
b = 0

massa = [] #Eixo Y
altura = [] #Eixo X

plt.plot(abscissa , ordenada , 'ro')
plt.xlabel("Deformação(m)" , fontsize = 'x-large')
plt.ylabel("Força(N)" , fontsize = 'x-large')
plt.title("Renato Guan")

for x in range(0,2):
  y = a*x+b
  massa.append(y)
  altura.append(x)

plt.plot(altura , massa , lw = 3)

plt.savefig("grafico_forca.png")