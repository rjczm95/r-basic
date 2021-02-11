

### DISTRIBUCIÓN GEOMÉTRICA ###


#Sea X = Geom(p = 0.1) la distribución que modela la 
#probabilidad de intentar abrir una puerta hasta conseguirlo

from scipy.stats import geom
import matplotlib.pyplot as plt
import numpy as np


p = 0.3 # probabilidad de abrir

#Estadísiticos para esta geométrica
mean, var, skew, kurt = geom.stats(p, moments = 'mvsk')
print("Media %f"%mean)
print("Varianza %f"%var)
print("Sesgo %f"%skew)
print("Curtosis %f"%kurt)


#Hacemos un gráfico
fig, ax = plt.subplots(1,1)

#genera los valores del eje x
x = np.arange(geom.ppf(0.01,p), geom.ppf(0.99, p))

#Representación de la función de probabilidad
ax.plot(x, geom.pmf(x, p), 'bo', ms = 8, 
	label = "Función de probabilidad de Geom(0.3)")
#Generamos las líneas verticales del eje x al valor de y
ax.vlines(x,0,geom.pmf(x,p),  colors = 'b', 
	lw = 4, alpha = 0.5)

#Agregamos una distribución teórica de la función de probabilidad
#Versión congelada (frozen)
rv = geom(p)
ax.vlines(x,0,rv.pmf(x), colors = 'k', 
	linestyles = '--', lw = 1, label = "Frozen PMF")
ax.legend(loc = 'best')
plt.show()
plt.close()


#Representamos la función de distribución acumulada para
#esta distribución geométrixa
fig, ax = plt.subplots(1,1)
prob = geom.cdf(x,p)
ax.plot(x, prob, 'bo', ms = 8)
plt.title("Función de distribución acumulada para Geométrica")
plt.ylim(0,1*1.1)
plt.show()


#Representación de valores aleatorios generados con
#geom.rvs() en un histograma
fig, ax = plt.subplots(1,1)
r = geom.rvs(p, size = 10000)
plt.hist(r)
plt.title("Histograma de valores aleatorios \n según la distribución Geométrica")
plt.show()




