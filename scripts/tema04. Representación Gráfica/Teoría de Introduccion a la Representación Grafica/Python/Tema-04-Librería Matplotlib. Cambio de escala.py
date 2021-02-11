
## LIBRERÍA MATPLOTLIB.PYPLOT

# Cambio de escala

import matplotlib.pyplot as plt
import numpy as np 
#Permite anular las divisiones de uno de los ejes 
from matplotlib.ticker import NullFormatter


mu = 0.5
sd = 0.3
y = mu + sd * np.random.randn(10000)
#Filtrar los números para quedarnos con los valores entre 0 y 1
y = y[(y>0) & (y<1)]
#Ordenamos los nºs de forma creciente
y.sort()
x=np.arange(len(y))

plt.figure(1,figsize=(10,8))

""" ESCALA LINEAL """
## La escala va del orden de 1 en 1
plt.subplot(2,2,1)
#Gráfico de la distribución de frecuencias acumuladas
plt.plot(x,y) #escala lineal
plt.yscale("linear") #Es lo mismo que lo anterior
plt.xscale("linear")
plt.title("Escala Lineal")
plt.grid(True)

""" ESCALA SEMILOGARITMICA """
##La escala va del orden de 10 en 10
plt.subplot(2,2,2)
plt.plot(x,y)
#Pongo escala logaritmica en eje y (figura semilogaritmica)
plt.yscale("log")
plt.title("Escala Logarítmica")
plt.grid(True)

""" ESCALA LOG SIMÉTRICO """
#Es lo mismo pero también para valores negativos
plt.subplot(2,2,3)
#Le restamos la media para que aparezcan valores negativos
plt.plot(x,y-y.mean())
#Escala simétrico logaritmico
#linthreshy= indica a cada cuanto queremos las divisiones logaritmicas
plt.yscale("symlog", linthresh=0.01)
plt.title("Escala Log Simétrico")
plt.grid(True)

""" ESCALA LOGÍSTICA """
#Da información detallada del inicio y del final de las distribuciones
plt.subplot(2,2,4)
plt.plot(x,y)
#Escala logística
plt.yscale("logit")
plt.title("Escala Logistica")
plt.gca().yaxis.set_minor_formatter(NullFormatter()) #Figura actual, anula formate del eje y
plt.grid(True)

#Ajustar los ejes para que no se superpongan en la figura
#Utilliza plt.subplots_adjust()
plt.subplots_adjust(top=0.92,bottom=0.08,left=0.1,right=0.95,
	hspace = 0.35, wspace = 0.35)

plt.show()
plt.close()



