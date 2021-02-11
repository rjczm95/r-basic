
### HISTOGRAMAS EN PYTHON CON BIBLIOTECAS ###

# Útil para grandes volúmenes de datos y calcular el histograma matemático


##  1. CONSTRUCCIÓN DEL HISTOGRAMA - NumPy ##

# Entra en escena la función np.histogram() de NumPy

import numpy as np 

#Vamos a crear una sucesión de nºs aleatorios obtenida a 
#traves de la "distribución de Laplace"

#La "distribución de Laplace" es una modificación de la
#distribución normal y suele emplearse bastante

np.random.seed(2019)

# La función np.set_printoptions es muy útil
# Entre todos los parámetros elegibles para configurar
# el comportamiento de NumPy
# A la hora de imprimir nºs se puede delimitar la precisión
np.set_printoptions(precision=3)

#Estimamos la media (loc), la escala (scale) y el tamaño de la muestar (size)
x = np.random.laplace(loc=10, scale=3, size=1000)
print(x[:6])
print("")


# Ahora debemos agrupar la información en intervalos para
# poder trabajar con los datos.
# bin_edges = extremos de los intervalos
# hist = fAbs de cada uno de los intervalos
hist, bin_edges = np.histogram(x)

# Por defecto la función np.histogram() 
# utiliza 10 intervalos de la misma amplitud.

print(hist)
print("")
print(bin_edges)
print("")

# nº de extremos de intervalos (11) y nº de intervalos (10)
# Valores por defecto de np.histogram()
print(bin_edges.size, hist.size)
print("")

# Por defecto los intervalos son semiabiertos, es decir,
# cerrados por la izda y abiertos por la dcha, a excepción
# del último intervalo que está cerrado por ambos lados.

#El máximo (max_edge) y mínimo (min_edge) del array son:
max_edge = x.max()
min_edge = x.min()

# El nº de divisiones (n_bins) será 10.
n_bins = 10

#Por tanto los extremos de los intervalos (bin_edges) son:
bin_edges = np.linspace(start=min_edge, stop=max_edge, 
	num=n_bins+1, endpoint=True)

#Se obtienen los mismos datos que con np.histograms()
print(bin_edges)
print("")


# La función np.bincount() cuenta el nº de apariciones
# de cada uno de los datos dentro de los limites indicados.
#Solo vale para nºs enteros
x2 = (0,1,1,1,2,2,3,7,7,7,25)

bcount = np.bincount(x2)
print(bcount)
print("")

#Hacemos el histograma
# Pongo _ para que no aparezcan los extremos de los intervalos
hist2, _ = np.histogram(x2, range=(0,max(x2)), 
	bins=max(x2)+1)
print(hist2)
print("")

#Tanto np.histogram() como np.bincount() hacen los mismo
#cuando las observaciones son nºs enteros
print(np.array_equal(bcount, hist2))
print("")


#Hacer un diciconario agrupando los valores unicos como clave
#con las fAbs obtenidas anteriormente
print(dict(zip(np.unique(x2),bcount[bcount.nonzero()])))
print("")


##  2. VISUALIZACIÓN DE HISTOGRAMAS - Matplotlib y Pandas ##

### matplotlib.pytplot -> plt.hist()

import matplotlib.pyplot as plt

#Con matplotlib.pyplot hay funciones que nos permiten
#visulaizar los histogramas directamente a partir de lo
#obtenido con la función np.histogram()

#Datos de estudio
np.random.seed(2019)
np.set_printoptions(precision=3)
x = np.random.laplace(loc=10, scale=3, size=1000)
print(x[:6])
print("")

#La función plt.np.hist() de matplotlib.pyplot nos devuelve:
#  - Nº de elementos (n)
#  - Los intervalos/divisiones (bins)
#  - Patches
#bins="auto" da divisiones según algoritmos de Python

n, bins, patches = plt.hist(x=x, 
	bins="auto", 
	color="#0505a5",
	alpha=0.7,
	rwidth=0.85)
#Para generar un grid horizontal
plt.grid(axis="y", linewidth=0.5, alpha=0.5)
plt.xlabel("Valor")
plt.ylabel("Frecuencia absoluta")
plt.title("Histograma de frecuencias", fontname="Times New Roman Bold")
#Escrino en LaTeX la media y el factor de escala de la distribución
plt.text(-5,85, r"$\mu = 10, b = 3$")
#Poner los marcadores más bonitos en eje "y"
maxfreq=n.max()
plt.ylim(ymax=np.ceil(maxfreq/10)*10 if maxfreq%10 else +10)
plt.show()
plt.close()

#Frec. de cada intervalo
print(n)
print("")

#Extremos de las divisiones
print(bins)
print("")

#Es una lista de 58 objetos de división (histograma)
print(patches)
print("")


### pandas -> pd.Series().plot.hist()

import pandas as pd 

#El histograma de pandas se basa en su clase o sus objetos
#llamados series (colecciones de datos). pd.Series

#Generamos los datos como Series
size, scale = 1000, 10
data = pd.Series(np.random.gamma(scale, size=size))

#Dibujamos el histograma de los datos anteriores
data.plot.hist( bins=20, 
	rwidth=0.9, color="#d52675")
plt.title("Distribución Gamma")
plt.xlabel("Valores")
plt.ylabel("Frecuencias")
plt.grid(axis="y",alpha=0.4)
plt.show()

#Al emplear esta función sobre un DF genera un histograma
#para cada una de las columnas numéricas del mismo
