
## LIBRERÍA MATPLOTLIB.PYPLOT

#Múltiples gráficas en una figura

import numpy as np

import matplotlib.pyplot as plt

#plt.gca() para ejes
#plt.gcf() para gráficos

#En esta clase vamos a partir de la función f(x) para representarla
def f(x):
	return np.exp(-x)*np.cos(2*np.pi*x)

#Se definen dos intervalos de valores para f(x)
#Con cada intervalo se representarán dos gráficos
x1 = np.arange(0,5.0,0.1)
x2 = np.arange(0,5.0,0.2)


#pl.figure() por defecto es 1
#Indica el numero de figuras
#Cada figura puede tener x gráficos
plt.figure(1)
#Indica el número de filas y columnas para representar las gráficas
#plt.subplot(filas, columnas,posición de gráfico)
plt.subplot(2,1,1)
plt.plot(x1,f(x1),"ro",x2,f(x2),"k")
plt.subplot(2,1,2)
plt.plot(x2,f(x2),"g--")
plt.show()
plt.close()


plt.figure(1)
plt.subplot(2,1,1)
plt.plot([1,2,3])
plt.subplot(2,1,2)
plt.plot([4,5,6])
#Figura 2
plt.figure(2)
plt.plot([1,3,9,16])

#Modificar un subplot anterior
plt.figure(1)
plt.subplot(2,1,1)
#Poner titulo
plt.title("Esto es el primer titulo")
plt.show()
#Cierra la figura para que no consuma memoria
plt.close()