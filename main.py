import numpy
import pylab
import random
 
# quantidade de passos
n = 100
 
# 2 arrays com 0s, de tamanho n(passos)
x = numpy.zeros(n)
y = numpy.zeros(n)
 
# completando as coordenadas com variáveis aleatórias
for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
     
 
# plotando um gráfico
pylab.title("Random Walk ($n = " + str(n) + "$ passos)")
pylab.plot(x, y)

# salvando uma imagem .png do gráfico
pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)
pylab.show()