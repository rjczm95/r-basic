
## LIBRERÍA MATPLOTLIB.PYPLOT

# Añadir textos al gráfico

import matplotlib.pyplot as plt
import numpy as np 

""" TEORÍA """

# La figura en matplotlib es una figura de representación o ventana
# es donde aparecen las representaciones gráficas o ejes

# Los ejes o axis son el rectángulo donde va el dibujo o representación gráfica
# van los ejes, la curva o punto dibujado y demás

# plt.hold() hace que cada gráfico borre el anterior y 
# permite dibujar un nuevo eje sobre la misma figura (obsoleta)

# plt.subplot(filas, columnas, posición) permite representar 
# más de un eje en la misma figura

## FIN DE TEORÍA



# Vamos a trabajar con el HISTOGRAMA DE FRECUENCIAS
# Este nuevo tipo de gráfico

#Establecer una distribución aleatoría con mu media y la 
#desviación típica sigma
mu = 100
sigma = 20
#Generamos la distribución con np.random.randn()
#Es la distribución normal (campana de Gauss) de 10.000 datos
x = mu + sigma * np.random.randn(10000)

# Generamos el histograma que devuelve:
#  - n: nº de elementos que forman parte de histograma
#  - bins: divisiones de los datos para generar las barras
#  - patches:cada uno de los conjuntos de datos generados
# La istrucción que genera el histograma es:
# plt.hist(valores,nº divisiones,otros parámetros)
hist1 = plt.hist(x,50, facecolor = "g", alpha =0.6)
plt.show()
plt.close()

#Al usar el parámetro density=True se genera una gráfica normalizada a 1
#De este modo la suma de todas las barras da 1
hist2 = plt.hist(x,50, density=True,facecolor = "g", alpha =0.6)
plt.xlabel("Cociente Intelectual", fontsize = 10,color="green") #fontsize para indicar tamaño de letra
plt.ylabel("Probabilidad",fontsize=10,color="green")
plt.title(r"HISTOGRAMA DE COCIENTE INTELECTUAL ($N ( \mu, \sigma)$)")
#Colocar texto en medio del gráfico
#al pone r"$(expresión)$" se escribe en LaTeX
plt.text(35,0.017,r"$ \mu = 100 , \sigma = 20 $")
#Generar un grid con plt.grid(True)
plt.axis([20,180,0,0.025])
plt.grid(True)
plt.show()
plt.close()

#figsize =(ancho, alto), para el tamaño de la figura
#dpi = pixeles/pulgada,para definir la calidad de pixeles por pulgadas
plt.figure(figsize=(10,6),dpi=90)
plt.subplot(1,1,1)
#Definir una secuencia y ver la función coseno de la misma
seq1=np.arange(0,10*np.pi,0.01)
y=np.cos(seq1)
plt.plot(seq1,y, lw=2.0)
#plt.annotate() para insertar un texto
#con arrowprops=dict() se indica que queremos que una flecha señale al punto xy
plt.annotate("Máximo Local", xy=(4*np.pi,1), xytext=(15,1.5),
	arrowprops=dict(facecolor="black", shrink=0.05,width=0.8))
plt.ylim(-2,2)
plt.xlabel(r"Ángulo $x$")
plt.ylabel(r"Coseno del ángulo $x$ ($\cos {x}$)")
plt.grid(True)
plt.show()
plt.close()