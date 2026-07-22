import math
import matplotlib.pyplot as plt

fig = plt.figure()          




X=[0.02539,0.03830,0.05556,0.06927,0.08701]                
Y=[1.56,2.4,3.47,4.33,5.4]                  
plt.plot(X,Y,'ro')




x = math.pi.linspace(0.0200,0.10, num = 5)          
y=  62.24*x                                        
plt.plot(x,y,'b-', lw=1.5)




plt.xlabel('Corrente (A)')
plt.ylabel('Potencial (V)')
plt.title('i versus V - Guilherme Martins')                          




fig.savefig('graficoixV.png')